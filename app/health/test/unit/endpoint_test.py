import json

import pytest
from src import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_returns_200_successful(client):
    # Assign
    expected = 200

    # Act
    actual = client.get("/health").status_code

    # Assert
    assert actual == expected


def test_health_returns_healthy_msg_successful(client):
    # Assign
    expected = "healthy!"

    # Act
    actual = json.loads(client.get("/health").data)

    # Assert
    assert actual == expected
