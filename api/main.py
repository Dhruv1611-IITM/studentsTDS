from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from JSON into a dictionary
MARKS_FILE ="q-vercel-python.json"
students = {}

with open(MARKS_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)
    students = {entry["name"]: entry["marks"] for entry in data}

def get_marks(name: List[str] = Query(...)):
    """Fetch student marks for the given names."""
    result = [students.get(n, None) for n in name]
    return {"marks": result}

