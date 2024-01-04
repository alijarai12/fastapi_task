from fastapi import FastAPI
from core.config import settings
from pydantic import BaseModel
from typing import Optional


app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)


class Student(BaseModel):
    name: str
    roll: Optional[str] = None
    address: str
    grade: Optional[float] = None


@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI🚀"}



@app.post("/student")
def create_student(student: Student):
    return student

@app.get("/student/{std_id}")
def get_student(std_id: int):
    return {"std_id": std_id}
