
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Temporary "database" (replace with SQLAlchemy later)
tasks_db = []

class Task(BaseModel):
    title: str
    description: str | None = None
    status: str = "pending"  # or "completed"

# Create a task
@app.post("/tasks")
def create_task(task: Task):
    tasks_db.append(task.dict())
    return {"message": "Task created!", "task": task}

# Get all tasks
@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks_db}

# Get a single task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    try:
        return tasks_db[task_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")