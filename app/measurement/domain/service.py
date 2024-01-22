import uuid
from datetime import datetime
from math import radians, cos, degrees, asin, sin
from typing import List, Tuple

from src.measurement.data.repo import MeasurementRepo
from src.measurement.domain.entity import MeasurementEntity


class MeasurementService:
    def __init__(self, repo: MeasurementRepo = None):
        self.repo = repo or MeasurementRepo()

    @staticmethod
    def document_to_entity(document: dict) -> MeasurementEntity:
        id_ = str(uuid.uuid4())[:8]
        created_at = updated_at = datetime.utcnow()

        return MeasurementEntity(
            id_=id_,
            created_at=created_at,
            updated_at=updated_at,
            archived=False,
            recorded_at=document["recorded_at"],
            city=document["city"],
            country=document["country"],
            latitude=document["latitude"],
            longitude=document["longitude"],
            pollutant=document["pollutant"],
            value=document["value"],
        )

    def upsert(self, document: dict) -> None:
        entity = self.document_to_entity(document=document)
        self.repo.upsert(entity=entity)

    def retrieve_by_pollutant(self, pollutant: str) -> List[MeasurementEntity]:
        return self.repo.retrieve_by_pollutant(pollutant=pollutant)

    def retrieve_by_country(
        self, pollutant: str, country: str
    ) -> List[MeasurementEntity]:
        return self.repo.retrieve_by_country(pollutant=pollutant, country=country)

    def retrieve_by_city(
        self, pollutant: str, country: str, city: str
    ) -> List[MeasurementEntity]:
        return self.repo.retrieve_by_city(
            pollutant=pollutant, country=country, city=city
        )

    @staticmethod
    def _calculate_bounding_box(
        latitude: float, longitude: float, radius: float
    ) -> Tuple[float, float, float, float]:
        earth_radius = 6371  # km

        # convert latitude and longitude to radians
        lat_rad = radians(latitude)
        lon_rad = radians(longitude)

        # calculate the radius in radians
        rad = radius / earth_radius

        # calculate min/max latitudes
        min_lat = lat_rad - rad
        max_lat = lat_rad + rad

        # calculate the difference in longitude
        delta_lon = asin(sin(rad) / cos(lat_rad))

        # calculate min/max longitudes
        min_lon = lon_rad - delta_lon
        max_lon = lon_rad + delta_lon

        # convert back to degrees
        min_lat = degrees(min_lat)
        max_lat = degrees(max_lat)
        min_lon = degrees(min_lon)
        max_lon = degrees(max_lon)

        return min_lat, max_lat, min_lon, max_lon

    def retrieve_by_area(
        self, pollutant: str, latitude: float, longitude: float, radius: float
    ) -> List[MeasurementEntity]:
        min_lat, max_lat, min_lon, max_lon = self._calculate_bounding_box(
            latitude, longitude, radius
        )
        return self.repo.retrieve_by_area(
            pollutant=pollutant,
            min_lat=min_lat,
            max_lat=max_lat,
            min_lon=min_lon,
            max_lon=max_lon,
        )
