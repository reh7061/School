# Book CRUD API

This is a simple API for performing CRUD (Create, Read, Update, Delete) operations on a collection of books. It is built using Python, Flask, and SQLAlchemy.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x  
- pip (Python package installer)
- flask 
    ```bash
    python -m pip install Flask Flask-SQLAlchemy
---

## Running
    python main.py

The API will now be running and accessible at:
http://127.0.0.1:5000

## API Endpoints
The below are examples using windows command prompt with curl. Since `cmd.exe` uses different formatting, it may not work on other OS.
### 1. Create a Book
Adds a new book record to the database.
* Method: `POST`
* URL: `/books`
* Body (raw JSON): 
```bash
{
    "book_name": "Naruto",
    "author": "Masashi Kishimoto",
    "publisher": "Shueisha"
}
```
Example `curl`: 
```
curl -X POST -H "Content-Type: application/json" -d "{\"book_name\": \"Naruto\", \"author\": \"Masashi Kishimoto\", \"publisher\": \"Shueisha\"}" http://127.0.0.1:5000/books
```
Success Response: `{ "id": 1}`

---
## 2. Get Books
Retrieves a list of all books in the database.
* Method: `GET`
* URL: `/books`
* Example `curl`: **curl http://127.0.0.1:5000/books**

## 3. Get Book by ID
Retrieves a single book record by its unique ID.
* URL: `/books/<id>`
* Example: **curl http://127.0.0.1:5000/books/1**

## 4. Update a Book
Updates the details of an existing book by its ID.
* Method: `PUT`
* URL: `/books/<id>`
* Body:
```
{
    "book_name": "Naruto Vol. 1",
    "author": "Masashi Kishimoto",
    "publisher": "VIZ Media"
}
```

Example: 
```
curl -X PUT -H "Content-Type: application/json" -d "{\"book_name\": \"Naruto Vol. 1\", \"author\": \"Masashi Kishimoto\", \"publisher\": \"VIZ Media\"}" http://127.0.0.1:5000/books/1
```

**Response**: `{ "message": "Book updated successfully." }`

---

## 5. Delete a Book
Deletes a book record from the database by its ID.
* Method: `DELETE`
* URL: `/books/<id>`
* Example: **curl -X DELETE http://127.0.0.1:5000/books/1**

**Reponse:** `{ "message": "Book deleted successfully." }`