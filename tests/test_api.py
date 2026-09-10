from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_measurement_analysis() -> None:
    response = client.post(
        "/measurements/analyse",
        json={
            "name": "brake_disc_temperature",
            "unit": "degC",
            "values": [412.4, 418.1, 415.7, 421.0],
            "reference": 416.0,
            "tolerance": 6.0,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["count"] == 4
    assert data["mean"] == 416.8
    assert data["minimum"] == 412.4
    assert data["maximum"] == 421.0
    assert data["within_tolerance"] is True


def test_out_of_tolerance_measurement() -> None:
    response = client.post(
        "/measurements/analyse",
        json={
            "name": "shaft_diameter",
            "unit": "mm",
            "values": [25.01, 25.02, 25.30],
            "reference": 25.0,
            "tolerance": 0.05,
        },
    )

    assert response.status_code == 200
    assert response.json()["within_tolerance"] is False


def test_empty_values_are_rejected() -> None:
    response = client.post(
        "/measurements/analyse",
        json={
            "name": "pressure",
            "unit": "bar",
            "values": [],
        },
    )

    assert response.status_code == 422