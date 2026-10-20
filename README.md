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

1. Install Python and PostgreSQL.
2. Create a PostgreSQL database named `taskmanager_db` and configure the required `tasks` table.
3. Create and activate a Python virtual environment.
4. Install the dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root containing:

   ```text
   DB_PASSWORD=your_actual_postgres_password
   ```

   Replace the placeholder with your local PostgreSQL password. Never commit or upload the `.env` file.

## Run the API

```powershell
python -m uvicorn src.main:app --reload --port 8001
```

Open http://127.0.0.1:8001/docs to explore and test the API.

## Run Tests

```powershell
python -m pytest -v
```

## Learning Outcome

Learned how to connect FastAPI to PostgreSQL, implement database-backed CRUD operations, and test API endpoints.
