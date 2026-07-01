from fastapi import FastAPI

app = FastAPI()

# --- First API Route ---
@app.get("/")
def get():
    return {"message": "This is my fast api app"}

# --- New Route with hardcoded data ---
@app.get("/view")
def view():
    # Assign the list of dictionaries to the students variable
    students = [
        {
            "id": 1,
            "name": "Nitish",
            "age": 23,
            "course": "MTECH"
        },
        {
            "id": 2,
            "name": "Yash",
            "age": 21,
            "course": "BSCCS"
        }
    ]

    return students