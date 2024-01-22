import json
from datetime import datetime

import requests

from src import app
from src.measurement.domain.service import MeasurementService


# This function makes a request to the OpenAQ API to fetch data for a specific country.
# The response is converted from JSON to a Python dictionary and returned.
def fetch_open_aq_by_country(country: str) -> dict:
    url = f"https://api.openaq.org/v2/locations?country={country}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return json.loads(response.content)


# This function ingests data from the OpenAQ API into AirQualityExplorer.
# It loops through the results from the OpenAQ API, extracting relevant information for each result.
# The information is used to create a document, which is then passed to the 'upsert' method of the 'MeasurementService'.
# This either inserts a new document into the database, or updates an existing one.
def ingest_open_aq(data: dict) -> None:
    for result in data["results"]:
        for parameter in result["parameters"]:
            with app.app_context():
                service = MeasurementService()
                document = {
                    "city": result["city"],
                    "country": result["country"],
                    "latitude": result["coordinates"]["latitude"]
                    if result["coordinates"]
                    else None,
                    "longitude": result["coordinates"]["longitude"]
                    if result["coordinates"]
                    else None,
                    "pollutant": parameter["parameter"].upper(),
                    "value": float(parameter["lastValue"]),
                    "recorded_at": datetime.strptime(
                        parameter["lastUpdated"], "%Y-%m-%dT%H:%M:%S%z"
                    ),
                }
                service.upsert(document=document)


# These functions are similar to each other, but are tailored to fetch data for specific countries.
# They log the initiation of the process, fetch data from OpenAQ, and pass the data to the 'ingest_open_aq' function.
def ingest_no_open_aq():
    app.logger.info("Ingesting NO Measurements from OpenAQ.")
    data = fetch_open_aq_by_country("NO")
    ingest_open_aq(data=data)
    app.logger.info("Ingestion of NO Measurements from OpenAQ complete.")


def ingest_se_open_aq():
    app.logger.info("Ingesting SE Measurements from OpenAQ.")
    data = fetch_open_aq_by_country("SE")
    ingest_open_aq(data=data)
    app.logger.info("Ingestion of SE Measurements from OpenAQ complete.")


def ingest_dk_open_aq():
    app.logger.info("Ingesting DK Measurements from OpenAQ.")
    data = fetch_open_aq_by_country("DK")
    ingest_open_aq(data=data)
    app.logger.info("Ingestion of DK Measurements from OpenAQ complete.")


def ingest_fi_open_aq():
    app.logger.info("Ingesting FI Measurements from OpenAQ.")
    data = fetch_open_aq_by_country("FI")
    ingest_open_aq(data=data)
    app.logger.info("Ingestion of FI Measurements from OpenAQ complete.")


def ingest_is_open_aq():
    app.logger.info("Ingesting IS Measurements from OpenAQ.")
    data = fetch_open_aq_by_country("IS")
    ingest_open_aq(data=data)
    app.logger.info("Ingestion of IS Measurements from OpenAQ complete.")
