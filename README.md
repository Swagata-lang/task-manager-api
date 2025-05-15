# Task Manager API

## Endpoints
| Method | Path | Description |
|--------|------|-------------|
| POST   | `/tasks` | Create new task |
| GET    | `/tasks` | List all tasks |

## Sample Request
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Example"}'
```