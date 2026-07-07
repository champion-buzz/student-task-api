# Student Task API

This is a small backend project built with FastAPI. I made it as a simple task tracker for school or portfolio work.

## Why I Built It

I wanted one project that shows basic backend skills:

- creating API routes
- using request and response models
- returning JSON
- handling missing data
- writing simple tests

The app stores tasks in memory, so it does not need a database to run.

## Features

- Health check route
- List all tasks
- Create a new task
- Get one task by ID
- Return a `404` error when a task is not found
- Tests with `pytest`

## Tech Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest

## Project Files

```text
app.py              FastAPI application
test_app.py         Backend tests
requirements.txt    Python dependencies
README.md           Project notes
```

## API Routes

| Method | Route | What it does |
| --- | --- | --- |
| `GET` | `/` | Returns a welcome message |
| `GET` | `/health` | Checks if the API is running |
| `GET` | `/tasks` | Lists all tasks |
| `POST` | `/tasks` | Creates a task |
| `GET` | `/tasks/{task_id}` | Gets one task |

## How To Run

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app:app --reload
```

Open the docs:

```text
http://127.0.0.1:8000/docs
```

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Finish README","course":"Portfolio","done":false}'
```

## Run Tests

```bash
pytest
```

## What I Learned

This project helped me practice how backend routes work and how to test API behavior. If I improved it later, I would add a real database and user login.
