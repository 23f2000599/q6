from fastapi import FastAPI, Query
import json

app = FastAPI()

# Load the data (make sure the correct path to your JSON file is used)
with open("api/q-vercel-python.json", "r") as file:
    marks_list = json.load(file)

# Convert the list to a dictionary for faster lookups
marks_data = {entry["name"]: entry["marks"] for entry in marks_list}

@app.get("/api")
def get_marks(name: str = Query(...)):
    # Fetch the marks for the provided name
    marks = marks_data.get(name)
    
    # If no marks found, return a message indicating that
    if marks is None:
        return {"message": f"No data available for name: {name}"}
    
    return {"marks": [marks]}

