from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
from pathlib import Path

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from JSON file
MARKS_FILE = Path("E:/TDS/students/data/q-vercel-python.json")
students = {}

try:
    with open(MARKS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        students = {entry["name"]: entry["marks"] for entry in data}
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading student data: {e}")

@app.get("/api")
def get_marks(name: List[str] = Query(None)):
    """Fetch student marks for the given names."""
    if not name:
        return {"error": "No names provided"}
    
    result = [students.get(n, None) for n in name]
    return {"marks": result}



