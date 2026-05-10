import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }


# Define a test function for adding a new sheep
def test_add_sheep():
    # TODO: Prepare the new sheep data in a dictionary format.
    new_sheep = {
        "id": 7,
        "name": "Sully",
        "breed": "Suffolk",
        "sex": "ram"
    }

    # TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
    response = client.post("/sheep/", json=new_sheep)

    # TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep

    # TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    get_response = client.get(f"/sheep/{new_sheep['id']}")
    assert get_response.status_code == 200
    assert get_response.json() == new_sheep


# Extra Credit: Delete Sheep Test
def test_delete_sheep():
    response = client.delete("/sheep/6")
    assert response.status_code == 204

    get_response = client.get("/sheep/6")
    assert get_response.status_code == 404


# Extra Credit: Update Sheep Test
def test_update_sheep():
    updated_data = {
        "id": 2,
        "name": "Blondie Updated",  # Changed the name
        "breed": "Polypay",
        "sex": "ram"
    }

    response = client.put("/sheep/2", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data

    get_response = client.get("/sheep/2")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Blondie Updated"


# Extra Credit: Read All Sheep Test
def test_read_all_sheep():
    response = client.get("/sheep/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    assert "id" in data[0]
    assert "name" in data[0]
    assert "breed" in data[0]
    assert "sex" in data[0]