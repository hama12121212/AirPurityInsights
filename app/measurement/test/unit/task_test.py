import json
from unittest.mock import patch
from datetime import datetime, timezone

import requests_mock

from src.measurement.domain.service import MeasurementService
from src.measurement.domain.task import (
    fetch_open_aq_by_country,
    ingest_open_aq,
    ingest_no_open_aq,
    ingest_se_open_aq,
    ingest_dk_open_aq,
)


# Test case for 'fetch_open_aq_by_country' function
def test_fetch_open_aq_by_country__requests_made_and_response_returned_successfully():
    # Assign
    expected = {"results": []}
    with requests_mock.Mocker() as m:
        m.get(
            "https://api.openaq.org/v2/locations?country=NO", text=json.dumps(expected)
        )

        # Act
        actual = fetch_open_aq_by_country("NO")

        # Assert
        assert actual == expected


# Test case for 'ingest_open_aq' function
@patch.object(MeasurementService, "upsert")
def test_ingest_open_aq__upsert_method_called_successfully(mock_upsert):
    # Assign
    data = {
        "results": [
            {
                "city": "Oslo",
                "country": "NO",
                "coordinates": {"latitude": 0, "longitude": 0},
                "parameters": [
                    {
                        "parameter": "pm2.5",
                        "lastValue": 2.5,
                        "lastUpdated": datetime.now(timezone.utc).strftime(
                            "%Y-%m-%dT%H:%M:%S%z"
                        ),
                    }
                ],
            }
        ]
    }

    # Act
    ingest_open_aq(data)

    # Assert
    assert mock_upsert.called


# Test case for 'ingest_no_open_aq' function
@patch("src.measurement.domain.task.fetch_open_aq_by_country")
@patch("src.measurement.domain.task.ingest_open_aq")
def test_ingest_no_open_aq__data_fetched_and_ingested_successfully(
    mock_ingest_open_aq, mock_fetch_open_aq_by_country
):
    # Act
    ingest_no_open_aq()

    # Assert
    mock_fetch_open_aq_by_country.assert_called_with("NO")
    assert mock_ingest_open_aq.called


# Test case for 'ingest_se_open_aq' function
@patch("src.measurement.domain.task.fetch_open_aq_by_country")
@patch("src.measurement.domain.task.ingest_open_aq")
def test_ingest_se_open_aq__data_fetched_and_ingested_successfully(
    mock_ingest_open_aq, mock_fetch_open_aq_by_country
):
    # Act
    ingest_se_open_aq()

    # Assert
    mock_fetch_open_aq_by_country.assert_called_with("SE")
    assert mock_ingest_open_aq.called


# Test case for 'ingest_dk_open_aq' function
@patch("src.measurement.domain.task.fetch_open_aq_by_country")
@patch("src.measurement.domain.task.ingest_open_aq")
def test_ingest_dk_open_aq__data_fetched_and_ingested_successfully(
    mock_ingest_open_aq, mock_fetch_open_aq_by_country
):
    # Act
    ingest_dk_open_aq()

    # Assert
    mock_fetch_open_aq_by_country.assert_called_with("DK")
    assert mock_ingest_open_aq.called
