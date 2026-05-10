from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    sheep = db.get_sheep(id)
    if not sheep:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return sheep

# Main Task: Add Sheep
@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")
    db.data[sheep.id] = sheep
    return sheep

# Extra Credit: Delete Sheep
@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id: int):
    try:
        db.delete_sheep(id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Sheep not found")

@app.put("/sheep/{id}", response_model=Sheep)
def update_sheep(id: int, sheep: Sheep):
    try:
        return db.update_sheep(id, sheep)
    except ValueError:
        raise HTTPException(status_code=404, detail="Sheep not found")

@app.get("/sheep/", response_model=list[Sheep])
def read_all_sheep():
    # Returning the values as a list is standard for REST APIs returning collections
    return list(db.get_all_sheep().values())