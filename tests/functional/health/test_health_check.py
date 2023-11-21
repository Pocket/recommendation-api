from fastapi.testclient import TestClient

from app.main import app


class TestHealthCheck:
    client: TestClient = TestClient(app)

    def test_healthy_status(self):
        response = self.client.get("/health-check")
        assert response.status_code == 200
        assert response.json() == {"status": "HEALTHY"}
