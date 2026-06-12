# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework. Students will learn how to define endpoints, handle JSON requests and responses, and use path and query parameters.

## 📝 Tasks

### 🛠️ Create REST API endpoints

#### Description

Build a FastAPI application with multiple endpoints for managing a list of items. Include endpoints for listing items, retrieving a single item, creating a new item, updating an existing item, and deleting an item.

#### Requirements

Completed program should:

- Define a FastAPI app with at least these routes: `GET /items`, `GET /items/{item_id}`, `POST /items`, `PUT /items/{item_id}`, and `DELETE /items/{item_id}`.
- Accept and return JSON data.
- Use path parameters to identify specific items and query parameters to filter or sort the results.
- Validate input data using Pydantic models.
- Return appropriate HTTP status codes for success and error cases.

## ✅ Starter files

- Starter code: `assignments/fastapi-rest-apis/starter-code.py`

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def list_items():
    return [{"id": 1, "name": "Item A"}]
```
