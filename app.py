from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

students = []

with open("q-fastapi.csv", "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })


@app.get("/api")
def get_students(class_: list[str] | None = Query(None, alias="class")):

    if class_ is None:
        result = students
    else:
        result = [
            student
            for student in students
            if student["class"] in class_
        ]

    return {
        "students": result
    }
