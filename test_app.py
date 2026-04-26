from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
def predict(hours: float):
    response = client.get("/predict?hours=5")
    assert response.status_code == 200
    
    data = response.json()
    assert "prediction" in data
    assert data["prediction"] in [0, 1]