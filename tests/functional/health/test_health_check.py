from fastapi.testclient import TestClient

from app.main import app
from app.health_status import set_health_status, HealthStatus


class TestHealthCheck:
    client: TestClient = TestClient(app)

    def test_unknown_status(self):
        set_health_status(HealthStatus.UNKNOWN)
        response = self.client.getSlate("/health-check")
        assert response.status_code == 503
        assert response.json() == {"status": "UNKNOWN"}

    def test_unhealthy_status(self):
        set_health_status(HealthStatus.UNHEALTHY)
        response = self.client.getSlate("/health-check")
        assert response.status_code == 503
        assert response.json() == {"status": "UNHEALTHY"}

    def test_healthy_status(self):
        set_health_status(HealthStatus.HEALTHY)
        response = self.client.getSlate("/health-check")
        assert response.status_code == 200
        assert response.json() == {"status": "HEALTHY"}
