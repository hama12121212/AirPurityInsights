from unittest.mock import patch
from src.measurement.domain.service import MeasurementService
from src.measurement.domain.entity import MeasurementEntity
from datetime import datetime


@patch("src.measurement.data.repo.MeasurementRepo.upsert")
def test_upsert_calls_repo_upsert_once(mock_upsert):
    document = {
        "recorded_at": datetime.utcnow(),
        "city": "Oslo",
        "country": "NO",
        "latitude": 59.9139,
        "longitude": 10.7522,
        "pollutant": "PM2.5",
        "value": 2.5,
    }

    # Assign
    service = MeasurementService()

    # Act
    service.upsert(document)

    # Assert
    mock_upsert.assert_called_once()


@patch("src.measurement.data.repo.MeasurementRepo.retrieve_by_pollutant")
def test_retrieve_by_pollutant_returns_one_entity_successful(
    mock_retrieve_by_pollutant,
):
    # Mock
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
            pollutant="PM2.5",
            value=2.5,
        )
    ]

    # Assign
    service = MeasurementService()
    expected = 1

    # Act
    actual = len(service.retrieve_by_pollutant("PM2.5"))

    # Assert
    assert actual == expected


@patch("src.measurement.data.repo.MeasurementRepo.retrieve_by_country")
def test_retrieve_by_country_returns_one_entity_successful(mock_retrieve_by_country):
    mock_retrieve_by_country.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Trondheim",
            country="NO",
            latitude=63.4468,
            longitude=10.4219,
            pollutant="PM2.5",
            value=2.5,
        )
    ]

    # Assign
    service = MeasurementService()
    expected = 1
    pollutant = "PM2.5"

    # Act
    actual = len(service.retrieve_by_country(pollutant, "NO"))

    # Assert
    assert actual == expected


@patch("src.measurement.data.repo.MeasurementRepo.retrieve_by_city")
def test_retrieve_by_city_returns_one_entity_successful(mock_retrieve_by_city):
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
            pollutant="PM2.5",
            value=2.5,
        )
    ]

    # Assign
    service = MeasurementService()
    expected = 1
    pollutant = "PM2.5"

    # Act
    actual = len(service.retrieve_by_city(pollutant, "NO", "Oslo"))

    # Assert
    assert actual == expected


def test_calculate_bounding_box_returns_correct_values():
    # Assign
    service = MeasurementService()
    latitude = 59.9139
    longitude = 10.7522
    radius = 5.0
    expected_min_lat = 59.8689
    expected_max_lat = 59.9589
    expected_min_lon = 10.6625
    expected_max_lon = 10.8419

    # Act
    min_lat, max_lat, min_lon, max_lon = service._calculate_bounding_box(
        latitude, longitude, radius
    )

    # Assert
    assert round(min_lat, 4) == expected_min_lat
    assert round(max_lat, 4) == expected_max_lat
    assert round(min_lon, 4) == expected_min_lon
    assert round(max_lon, 4) == expected_max_lon


@patch("src.measurement.data.repo.MeasurementRepo.retrieve_by_area")
def test_retrieve_by_area_returns_one_entity_successful(mock_retrieve_by_area):
    # Mock
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
            pollutant="PM2.5",
            value=2.5,
        )
    ]

    # Assign
    service = MeasurementService()
    expected = 1
    pollutant = "PM2.5"
    latitude = 59.9139
    longitude = 10.7522
    radius = 5.0

    # Act
    actual = len(service.retrieve_by_area(pollutant, latitude, longitude, radius))

    # Assert
    assert actual == expected


@patch("src.measurement.data.repo.MeasurementRepo.retrieve_by_area")
def test_retrieve_by_area_returns_no_entity_when_none_in_area(mock_retrieve_by_area):
    # Mock
    mock_retrieve_by_area.return_value = []

    # Assign
    service = MeasurementService()
    expected = 0
    pollutant = "PM2.5"
    latitude = 59.9139
    longitude = 10.7522
    radius = 5.0

    # Act
    actual = len(service.retrieve_by_area(pollutant, latitude, longitude, radius))

    # Assert
    assert actual == expected
