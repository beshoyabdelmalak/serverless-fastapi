from fastapi import testclient
from api.main import app

CLIENT = testclient.TestClient(app)

def test_root():
    response = CLIENT.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "from FastAPI & API Gateway"}