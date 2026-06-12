# 📘 Assignment: Building APIs with FastAPI and SQLite

## 🎯 Objective

Build a FastAPI application that stores and retrieves data using SQLite. Students will learn how to persist API data, define database models, and use CRUD operations with the FastAPI framework.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description

Build a FastAPI app that provides endpoints for managing a collection of books. Store book data in an SQLite database and use Pydantic models for request validation.

#### Requirements

Completed program should:

- Define a FastAPI app with routes for `GET /books`, `GET /books/{book_id}`, `POST /books`, `PUT /books/{book_id}`, and `DELETE /books/{book_id}`.
- Persist book data in an SQLite database.
- Use Pydantic models to validate request and response data.
- Return appropriate HTTP status codes for success and error cases.
- Handle database errors gracefully.

### 🛠️ Use SQLite persistence

#### Description

Create and initialize an SQLite database file, then read and write book records from the database using SQL or an ORM.

#### Requirements

Completed program should:

- Create an SQLite database file automatically if it does not exist.
- Store each book with `id`, `title`, `author`, and `year` fields.
- Update and delete records persistently.
- Keep the database schema simple and easy to understand for beginners.

## ✅ Starter files

- Starter code: `assignments/fastapi-sqlite/starter-code.py`

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/books")
def list_books():
    return [{"id": 1, "title": "My Book", "author": "Author", "year": 2024}]
```
