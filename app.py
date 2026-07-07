from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Student Task API")


class TaskCreate(BaseModel):
    title: str
    course: str
    done: bool = False


class Task(TaskCreate):
    id: int


tasks: list[Task] = [
    Task(id=1, title="Finish AI project folders", course="Portfolio", done=False),
    Task(id=2, title="Review README files", course="Portfolio", done=True),
]


@app.get("/")
def home() -> dict:
    return {"message": "Student Task API"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "task_count": len(tasks)}


@app.get("/tasks")
def list_tasks() -> list[Task]:
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate) -> Task:
    new_task = Task(id=len(tasks) + 1, **task.model_dump())
    tasks.append(new_task)
    return new_task


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
