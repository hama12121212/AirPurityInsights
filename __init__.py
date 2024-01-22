from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from flasgger import Swagger
from datetime import datetime, timedelta

from src.measurement.rest.spec import definitions

app = Flask(__name__, template_folder="visualization/templates")
app.config.from_object("src.config")
db = SQLAlchemy(app)
swagger = Swagger(
    app,
    template={
        "swagger": "2.0",
        "info": {
            "title": "API",
            "description": " A Flask API for fetching, processing, and visualizing real-time air quality data.",
            "version": "1.0",
        },
        "definitions": definitions,
    },
)

with app.app_context():
    from src.health.rest.endpoint import health
    from src.measurement.rest.endpoint import retrieve_by_pollutant
    from src.measurement.rest.endpoint import retrieve_by_country
    from src.measurement.rest.endpoint import retrieve_by_city
    from src.measurement.data.dao import MeasurementDAO
    from src.measurement.domain.task import ingest_no_open_aq
    from src.measurement.domain.task import ingest_se_open_aq
    from src.measurement.domain.task import ingest_dk_open_aq
    from src.measurement.domain.task import ingest_fi_open_aq
    from src.measurement.domain.task import ingest_is_open_aq
    from src.visualization.rest.endpoint import map
    from src.visualization.rest.endpoint import pollutant_map

    db.create_all()

    scheduler = APScheduler()
    scheduler.init_app(app)

    # Update the next_run_time for each scheduled task
    delay_minutes = 1  
    current_time = datetime.utcnow() + timedelta(minutes=delay_minutes)

    scheduler.add_job(
        id="Scheduled Ingestion NO OpenAQ",
        func=ingest_no_open_aq,
        trigger="cron",
        hour=3,  # Specify the desired hour (adjust as needed)
        minute=0,  # Specify the desired minute
        next_run_time=current_time,
    )

    scheduler.add_job(
        id="Scheduled Ingestion SE OpenAQ",
        func=ingest_se_open_aq,
        trigger="cron",
        hour=3,  # Specify the desired hour (adjust as needed)
        minute=0,  # Specify the desired minute
        next_run_time=current_time,
    )

    scheduler.add_job(
        id="Scheduled Ingestion DK OpenAQ",
        func=ingest_dk_open_aq,
        trigger="cron",
        hour=3,  # Specify the desired hour (adjust as needed)
        minute=0,  # Specify the desired minute
        next_run_time=current_time,
    )

    scheduler.add_job(
        id="Scheduled Ingestion FI OpenAQ",
        func=ingest_fi_open_aq,
        trigger="cron",
        hour=3,  # Specify the desired hour (adjust as needed)
        minute=0,  # Specify the desired minute
        next_run_time=current_time,
    )

    scheduler.add_job(
        id="Scheduled Ingestion IS OpenAQ",
        func=ingest_is_open_aq,
        trigger="cron",
        hour=3,  # Specify the desired hour (adjust as needed)
        minute=0,  # Specify the desired minute
        next_run_time=current_time,
    )

    scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)
