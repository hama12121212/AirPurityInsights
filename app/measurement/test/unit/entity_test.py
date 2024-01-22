import pytest
from datetime import datetime

from src.measurement.domain.entity import MeasurementEntity


@pytest.fixture
def measurement_entity():
    id_ = "216bb524"
    created_at = datetime.now()
    updated_at = created_at
    archived = False
    recorded_at = created_at
    city = "San Francisco"
    country = "US"
    latitude = 37.7749
    longitude = -122.4194
    pollutant = "CO2"
    value = 200.0

    entity = MeasurementEntity(
        id_,
        created_at,
        updated_at,
        archived,
        recorded_at,
        city,
        country,
        latitude,
        longitude,
        pollutant,
        value,
    )

    return (
        entity,
        id_,
        created_at,
        updated_at,
        archived,
        recorded_at,
        city,
        country,
        latitude,
        longitude,
        pollutant,
        value,
    )


def test_measurement_entity_id__initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        id_,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
    ) = measurement_entity
    expected = id_

    # Act
    actual = entity.id_

    # Assert
    assert actual == expected


def test_measurement_entity_created_at_initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        _,
        created_at,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
    ) = measurement_entity
    expected = created_at

    # Act
    actual = entity.created_at

    # Assert
    assert actual == expected


def test_measurement_entity_updated_at_initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        _,
        _,
        updated_at,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
    ) = measurement_entity
    expected = updated_at

    # Act
    actual = entity.updated_at

    # Assert
    assert actual == expected


def test_measurement_entity_archived_initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        _,
        _,
        _,
        archived,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
    ) = measurement_entity
    expected = archived

    # Act
    actual = entity.archived

    # Assert
    assert actual == expected


def test_measurement_entity_recorded_at_initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        _,
        _,
        _,
        _,
        recorded_at,
        _,
        _,
        _,
        _,
        _,
        _,
    ) = measurement_entity
    expected = recorded_at

    # Act
    actual = entity.recorded_at

    # Assert
    assert actual == expected


def test_measurement_entity_city_initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        _,
        _,
        _,
        _,
        _,
        city,
        _,
        _,
        _,
        _,
        _,
    ) = measurement_entity
    expected = city

    # Act
    actual = entity.city

    # Assert
    assert actual == expected


def test_measurement_entity_country_initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        _,
        _,
        _,
        _,
        _,
        _,
        country,
        _,
        _,
        _,
        _,
    ) = measurement_entity
    expected = country

    # Act
    actual = entity.country

    # Assert
    assert actual == expected


def test_measurement_entity_latitude_initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        latitude,
        _,
        _,
        _,
    ) = measurement_entity
    expected = latitude

    # Act
    actual = entity.latitude

    # Assert
    assert actual == expected


def test_measurement_entity_longitude_initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        longitude,
        _,
        _,
    ) = measurement_entity
    expected = longitude

    # Act
    actual = entity.longitude

    # Assert
    assert actual == expected


def test_measurement_entity_pollutant_initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        pollutant,
        _,
    ) = measurement_entity
    expected = pollutant

    # Act
    actual = entity.pollutant

    # Assert
    assert actual == expected


def test_measurement_entity_value_initialization_successful(measurement_entity):
    # Assign
    (
        entity,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        value,
    ) = measurement_entity
    expected = value

    # Act
    actual = entity.value

    # Assert
    assert actual == expected


def test_measurement_entity_string_representation_successful(measurement_entity):
    # Assign
    (
        entity,
        id_,
        created_at,
        updated_at,
        archived,
        recorded_at,
        city,
        country,
        latitude,
        longitude,
        pollutant,
        value,
    ) = measurement_entity

    expected = (
        f"{id_}\n"
        f"{created_at}\n"
        f"{updated_at}\n"
        f"{str(archived)}\n"
        f"{recorded_at}\n"
        f"{city}\n"
        f"{country}\n"
        f"{latitude}\n"
        f"{longitude}\n"
        f"{pollutant}\n"
        f"{value}\n"
    )

    # Act
    actual = str(entity)

    # Assert
    assert actual == expected


def test_measurement_entity_vars_representation_successful(measurement_entity):
    # Assign
    (
        entity,
        id_,
        created_at,
        updated_at,
        archived,
        recorded_at,
        city,
        country,
        latitude,
        longitude,
        pollutant,
        value,
    ) = measurement_entity

    expected = {
        "id_": id_,
        "created_at": created_at,
        "updated_at": updated_at,
        "archived": archived,
        "recorded_at": recorded_at,
        "city": city,
        "country": country,
        "latitude": latitude,
        "longitude": longitude,
        "pollutant": pollutant,
        "value": value,
    }

    # Act
    actual = vars(entity)

    # Assert
    assert actual == expected
