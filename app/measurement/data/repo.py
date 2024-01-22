from datetime import datetime
from typing import List

from src import db
from src.measurement.domain.entity import MeasurementEntity
from src.measurement.data.dao import MeasurementDAO


class MeasurementRepo:
    @staticmethod
    def _to_entity(dao: MeasurementDAO) -> MeasurementEntity:
        return MeasurementEntity(
            id_=dao.id_,
            created_at=dao.created_at,
            updated_at=dao.updated_at,
            archived=dao.archived,
            recorded_at=dao.recorded_at,
            city=dao.city,
            country=dao.country,
            latitude=dao.latitude,
            longitude=dao.longitude,
            pollutant=dao.pollutant,
            value=dao.value,
        )

    @staticmethod
    def _to_dao(entity: MeasurementEntity) -> MeasurementDAO:
        return MeasurementDAO(
            id_=entity.id_,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            archived=entity.archived,
            recorded_at=entity.recorded_at,
            city=entity.city,
            country=entity.country,
            latitude=entity.latitude,
            longitude=entity.longitude,
            pollutant=entity.pollutant,
            value=entity.value,
        )

    def upsert(self, entity: MeasurementEntity) -> None:
        dao = MeasurementDAO.query.filter(
            MeasurementDAO.recorded_at == entity.recorded_at,
            MeasurementDAO.city == entity.city,
            MeasurementDAO.country == entity.country,
            MeasurementDAO.latitude == entity.latitude,
            MeasurementDAO.longitude == entity.longitude,
            MeasurementDAO.pollutant == entity.pollutant,
            MeasurementDAO.value == entity.value,
        ).first()

        if dao is not None:
            dao.updated_at = datetime.utcnow()
        else:
            dao = self._to_dao(entity)

        db.session.add(dao)
        db.session.commit()

    def retrieve_by_pollutant(self, pollutant: str) -> List[MeasurementEntity]:
        daos = MeasurementDAO.query.filter(
            MeasurementDAO.pollutant == pollutant,
            MeasurementDAO.archived.is_(False),
        ).all()

        return [self._to_entity(dao) for dao in daos]

    def retrieve_by_country(
        self, pollutant: str, country: str
    ) -> List[MeasurementEntity]:
        daos = MeasurementDAO.query.filter(
            MeasurementDAO.pollutant == pollutant,
            MeasurementDAO.country == country,
            MeasurementDAO.archived.is_(False),
        ).all()

        return [self._to_entity(dao) for dao in daos]

    def retrieve_by_city(
        self, pollutant: str, country: str, city: str
    ) -> List[MeasurementEntity]:
        daos = MeasurementDAO.query.filter(
            MeasurementDAO.pollutant == pollutant,
            MeasurementDAO.country == country,
            MeasurementDAO.city == city,
            MeasurementDAO.archived.is_(False),
        ).all()

        return [self._to_entity(dao) for dao in daos]

    def retrieve_by_area(
        self,
        pollutant: str,
        min_lat: float,
        max_lat: float,
        min_lon: float,
        max_lon: float,
    ) -> List[MeasurementEntity]:
        daos = MeasurementDAO.query.filter(
            MeasurementDAO.pollutant == pollutant,
            MeasurementDAO.archived.is_(False),
            MeasurementDAO.latitude >= min_lat,
            MeasurementDAO.latitude <= max_lat,
            MeasurementDAO.longitude >= min_lon,
            MeasurementDAO.longitude <= max_lon,
        ).all()

        # return as entity objects
        return [self._to_entity(dao) for dao in daos]
