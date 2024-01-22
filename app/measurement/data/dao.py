from src import db


class MeasurementDAO(db.Model):
    __tablename__ = "measurement"
    id_ = db.Column(db.String(40), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    archived = db.Column(db.Boolean, default=False, nullable=False)
    recorded_at = db.Column(db.DateTime, nullable=False)
    city = db.Column(db.String(40), nullable=True)
    country = db.Column(db.String(40), nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    pollutant = db.Column(db.String(40), nullable=False)
    value = db.Column(db.Float, default=0.0, nullable=False)
