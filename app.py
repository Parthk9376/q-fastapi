from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv
from typing import Optional

app = FastAPI()

# Allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Read CSV
students = []

with open("q-fastapi.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })


@app.get("/api")
def get_students(class_: Optional[list[str]] = Query(default=None, alias="class")):
    if class_:
        filtered = [
            student for student in students
            if student["class"] in class_
        ]
    else:
        filtered = students

    return {"students": filtered}
