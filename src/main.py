
import os

import psycopg
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

# Load environment variables from the .env file
load_dotenv()

app = FastAPI(
    title="Task Manager API",
    description="A simple REST API to manage tasks using PostgreSQL",
    version="1.0.0"
)

# PostgreSQL database configuration
DB_CONFIG = {
    "dbname": "taskmanager_db",
    "user": "postgres",
    "password": os.getenv("DB_PASSWORD"),
    "host": "localhost",
    "port": 5432
}


# Model for creating a task
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)


# Model for updating a task
class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    completed: bool


# Model for API responses
class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool


# Get all tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, title, completed FROM tasks ORDER BY id"
            )
            rows = cur.fetchall()

    return [
        {"id": row[0], "title": row[1], "completed": row[2]}
        for row in rows
    ]


# Get one task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, title, completed FROM tasks WHERE id = %s",
                (task_id,)
            )
            row = cur.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "id": row[0],
        "title": row[1],
        "completed": row[2]
    }


# Create a new task
@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):
    title = task.title.strip()

    if not title:
        raise HTTPException(
            status_code=422,
            detail="Task title cannot be empty"
        )

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO tasks (title, completed)
                VALUES (%s, FALSE)
                RETURNING id, title, completed
                """,
                (title,)
            )
            row = cur.fetchone()

    return {
        "id": row[0],
        "title": row[1],
        "completed": row[2]
    }


# Update an existing task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
    title = task.title.strip()

    if not title:
        raise HTTPException(
            status_code=422,
            detail="Task title cannot be empty"
        )

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE tasks
                SET title = %s, completed = %s
                WHERE id = %s
                RETURNING id, title, completed
                """,
                (title, task.completed, task_id)
            )
            row = cur.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "id": row[0],
        "title": row[1],
        "completed": row[2]
    }


# Delete a task
@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(task_id: int):
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM tasks WHERE id = %s RETURNING id",
                (task_id,)
            )
            row = cur.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
