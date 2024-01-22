import json
from datetime import datetime

import pytest
from unittest.mock import patch
from src import app
from src.measurement.domain.entity import MeasurementEntity


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_pollutant")
def test_retrieve_measurement_pollutant_returns_200_successful(
    mock_retrieve_by_pollutant, client
):
    # Assign
    mock_retrieve_by_pollutant.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Oslo",
            country="NO",
            latitude=59.9139,
            longitude=10.7522,
            pollutant="PM25",
            value=2.5,
        ),
    ]
    expected = 200

    # Act
    actual = client.get("/measurement/PM25").status_code

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_pollutant")
def test_retrieve_measurement_pollutant_returns_measurements_successful(
    mock_retrieve_by_pollutant, client
):
    # Assign
    mock_retrieve_by_pollutant.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Oslo",
            country="NO",
            latitude=59.9139,
            longitude=10.7522,
            pollutant="PM25",
            value=2.5,
        ),
    ]
    expected = 1

    # Act
    response = client.get("/measurement/PM25")
    actual = len(json.loads(response.data))

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_pollutant")
def test_retrieve_measurement_pollutant_returns_404_when_no_entities(
    mock_retrieve_by_pollutant, client
):
    # Assign
    mock_retrieve_by_pollutant.return_value = []
    expected = 404

    # Act
    actual = client.get("/measurement/PM25").status_code

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_country")
def test_retrieve_measurement_country_returns_200_successful(
    mock_retrieve_by_country, client
):
    # Assign
    mock_retrieve_by_country.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Trondheim",
            country="NO",
            latitude=63.446827,
            longitude=10.421906,
            pollutant="PM25",
            value=2.5,
        ),
    ]
    expected = 200

    # Act
    actual = client.get("/measurement/PM25/NO").status_code

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_country")
def test_retrieve_measurement_country_returns_measurements_successful(
    mock_retrieve_by_country, client
):
    # Assign
    mock_retrieve_by_country.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Trondheim",
            country="NO",
            latitude=63.446827,
            longitude=10.421906,
            pollutant="PM25",
            value=2.5,
        ),
    ]
    expected = 1

    # Act
    response = client.get("/measurement/PM25/NO")
    actual = len(json.loads(response.data))

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_country")
def test_retrieve_measurement_country_returns_404_when_no_entities(
    mock_retrieve_by_country, client
):
    # Assign
    mock_retrieve_by_country.return_value = []
    expected = 404

    # Act
    actual = client.get("/measurement/PM25/NO").status_code

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_city")
def test_retrieve_measurement_city_returns_200_successful(
    mock_retrieve_by_city, client
):
    # Assign
    mock_retrieve_by_city.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Oslo",
            country="NO",
            latitude=59.9139,
            longitude=10.7522,
            pollutant="PM25",
            value=2.5,
        ),
    ]
    expected = 200

    # Act
    actual = client.get("/measurement/PM25/NO/Oslo").status_code

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_city")
def test_retrieve_measurement_city_returns_measurements_successful(
    mock_retrieve_by_city, client
):
    # Assign
    mock_retrieve_by_city.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Oslo",
            country="NO",
            latitude=59.9139,
            longitude=10.7522,
            pollutant="PM25",
            value=2.5,
        ),
    ]
    expected = 1

    # Act
    response = client.get("/measurement/PM25/NO/Oslo")
    actual = len(json.loads(response.data))

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_city")
def test_retrieve_measurement_city_returns_404_when_no_entities(
    mock_retrieve_by_city, client
):
    # Assign
    mock_retrieve_by_city.return_value = []
    expected = 404

    # Act
    actual = client.get("/measurement/PM25/NO/Oslo").status_code

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_area")
def test_retrieve_measurement_area_returns_200_successful(
    mock_retrieve_by_area, client
):
    # Assign
    mock_retrieve_by_area.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Oslo",
            country="NO",
            latitude=59.9139,
            longitude=10.7522,
            pollutant="PM25",
            value=2.5,
        ),
    ]
    expected = 200

    # Act
    actual = client.get("/measurement/PM25/59.9139/10.7522/100").status_code

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_area")
def test_retrieve_measurement_area_returns_measurements_successful(
    mock_retrieve_by_area, client
):
    # Assign
    mock_retrieve_by_area.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Oslo",
            country="NO",
            latitude=59.9139,
            longitude=10.7522,
            pollutant="PM25",
            value=2.5,
        ),
    ]
    expected = 1

    # Act
    response = client.get("/measurement/PM25/59.9139/10.7522/100")
    actual = len(json.loads(response.data))

    # Assert
    assert actual == expected


@patch("src.measurement.domain.service.MeasurementService.retrieve_by_area")
def test_retrieve_measurement_area_returns_404_when_no_entities(
    mock_retrieve_by_area, client
):
    # Assign
    mock_retrieve_by_area.return_value = []
    expected = 404

    # Act
    actual = client.get("/measurement/PM25/59.9139/10.7522/100").status_code

    # Assert
    assert actual == expected
