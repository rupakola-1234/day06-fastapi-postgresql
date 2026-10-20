# Day 6 — FastAPI Task Manager with PostgreSQL

## Project Overview
This project is a Task Manager REST API built using Python, FastAPI, and PostgreSQL. It stores tasks in a database and supports CRUD operations.

## Technologies Used
- Python
- FastAPI
- PostgreSQL
- Psycopg
- Pydantic
- Pytest

## Features
- Retrieve all tasks
- Retrieve a task by ID
- Create a new task
- Update an existing task
- Delete a task
- Store tasks persistently in PostgreSQL

## Project Structure
```text
day06-fastapi-postgresql/
├── src/
│   └── main.py
├── test_main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions
1. Create and activate a Python virtual environment.
2. Install dependencies:

   `python -m pip install -r requirements.txt`

3. Create a `.env` file in the project root and add your local PostgreSQL password:

   `DB_PASSWORD=your_actual_postgres_password`

   Replace the placeholder with your actual password. Do not upload the `.env` file to GitHub.

## Run the API
```powershell
python -m uvicorn src.main:app --reload --port 8001
```

Open `http://127.0.0.1:8001/docs` to explore and test the API.

## Run Tests
```powershell
python -m pytest -v
```

## Learning Outcome
Learned how to connect FastAPI to PostgreSQL, implement database-backed CRUD operations, and test API endpoints.
