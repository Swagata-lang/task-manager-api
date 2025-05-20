<<<<<<< HEAD
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import database

app = FastAPI()

# Create tables (only needed once)
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Updated POST endpoint
@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.DBTask(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Updated GET all endpoint
@app.get("/tasks", response_model=List[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return db.query(models.DBTask).all()

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(models.DBTask).filter(models.DBTask.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.model_dump().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.DBTask).filter(models.DBTask.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}
=======
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import database

app = FastAPI()

# Create tables (only needed once)
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Updated POST endpoint
@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.DBTask(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Updated GET all endpoint
@app.get("/tasks", response_model=List[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return db.query(models.DBTask).all()




@app.post(
    "/tasks",
    response_model=schemas.Task,
    summary="Create a new task",
    description="Adds a new task to the database with title, description, and status",
    tags=["Tasks"]  # Groups endpoints in docs
)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    ## Create Task
    Requires:
    - **title**: string (required)
    - **description**: string (optional)
    - **status**: string (default: "pending")

    Returns the created task with ID.
    """
    ...

    app = FastAPI(
    title="Task Manager API",
    description="## A simple task management system\n"
               "Supports CRUD operations with SQLite database",
    version="1.0.0",
    contact={
        "name": "SWAGATA RANJAN MOHAPATRA",
        "email": "officialswagata66@gmail.com",
    },
)
>>>>>>> bfef1c0f6358deab7beb4fe0a2d21cc9e05a6561
