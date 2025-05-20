# 📝 Task Manager API

A FastAPI-powered task management system with SQLite database.

## 🚀 Features
- CRUD operations for tasks
- SQLite database with SQLAlchemy ORM
- Pydantic data validation

## 🔧 Installation
```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api
python -m venv env
.\env\Scripts\activate  # Windows
pip install -r requirements.txt
```

## 🏃 Running the API
```bash
uvicorn main:app --reload
```
- Interactive Docs: http://localhost:8000/docs
- Raw API: http://localhost:8000/tasks

## 📚 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/tasks` | Create task |
| GET    | `/tasks` | List tasks |
| PUT    | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |

## 🧪 Testing
```bash
# Create task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Test"}'

# List tasks
curl http://localhost:8000/tasks
```

## 🏗 Project Structure
```
task-manager-api/
├── main.py           # API routes
├── database.py       # DB connection
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic models
└── README.md         # This file
```