from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3
from sqlite3 import Connection

app = FastAPI()
DATABASE_PATH = "assignments/fastapi-sqlite/books.db"

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

class BookCreate(BaseModel):
    title: str
    author: str
    year: int


def get_db() -> Connection:
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/books", response_model=List[Book])
def list_books() -> List[Book]:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, year FROM books")
    rows = cursor.fetchall()
    conn.close()
    return [Book(**dict(row)) for row in rows]


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, year FROM books WHERE id = ?", (book_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return Book(**dict(row))


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate) -> Book:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (book.title, book.author, book.year),
    )
    conn.commit()
    book_id = cursor.lastrowid
    conn.close()

    return Book(id=book_id, **book.dict())


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate) -> Book:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?",
        (book.title, book.author, book.year, book_id),
    )
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")

    conn.close()
    return Book(id=book_id, **book.dict())


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")

    conn.close()
    return {"detail": "Book deleted"}
