from src import app

from flask import jsonify

from src.measurement.domain.service import MeasurementService


@app.route("/measurement/<pollutant>", methods=["GET"])
def retrieve_by_pollutant(pollutant: str):
    """
    ---
    tags:
      - Measurement
    parameters:
      - name: pollutant
        in: path
        type: string
        required: true
        description: The pollutant to retrieve measurements for.
    responses:
      200:
        description: A list of measurements for the given pollutant.
        schema:
          type: array
          items:
            $ref: '#/definitions/Measurement'
      404:
        description: No measurements found for this pollutant.
    """
    service = MeasurementService()

    entities = service.retrieve_by_pollutant(pollutant=pollutant)

    if not entities:
        return jsonify({"message": "No measurements found for this pollutant."}), 404

    return jsonify([vars(entity) for entity in entities]), 200


@app.route("/measurement/<pollutant>/<country>", methods=["GET"])
def retrieve_by_country(pollutant: str, country: str):
    """
    ---
    tags:
      - Measurement
    parameters:
      - name: pollutant
        in: path
        type: string
        required: true
        description: The pollutant to retrieve measurements for.
      - name: country
        in: path
        type: string
        required: true
        description: The country to retrieve measurements for.
    responses:
      200:
        description: A list of measurements for the given pollutant in the specified country.
        schema:
          type: array
          items:
            $ref: '#/definitions/Measurement'
      404:
        description: No measurements found for this country.
    """
    service = MeasurementService()

    entities = service.retrieve_by_country(pollutant=pollutant, country=country)

    if not entities:
        return jsonify({"message": "No measurements found for this country."}), 404

    return jsonify([vars(entity) for entity in entities]), 200


@app.route("/measurement/<pollutant>/<country>/<city>", methods=["GET"])
def retrieve_by_city(pollutant: str, country: str, city: str):
    """
    ---
    tags:
      - Measurement
    parameters:
      - name: pollutant
        in: path
        type: string
        required: true
        description: The pollutant to retrieve measurements for.
      - name: country
        in: path
        type: string
        required: true
        description: The country to retrieve measurements for.
      - name: city
        in: path
        type: string
        required: true
        description: The city to retrieve measurements for.
    responses:
      200:
        description: A list of measurements for the given pollutant in the specified city.
        schema:
          type: array
          items:
            $ref: '#/definitions/Measurement'
      404:
        description: No measurements found for this city.
    """
    service = MeasurementService()

    entities = service.retrieve_by_city(pollutant=pollutant, country=country, city=city)

    if not entities:
        return jsonify({"message": "No measurements found for this city."}), 404

    return jsonify([vars(entity) for entity in entities]), 200


@app.route("/measurement/<pollutant>/<latitude>/<longitude>/<radius>", methods=["GET"])
def retrieve_by_area(pollutant: str, latitude: float, longitude: float, radius: float):
    """
    ---
    tags:
      - Measurement
    parameters:
      - name: pollutant
        in: path
        type: string
        required: true
        description: The pollutant to retrieve measurements for.
      - name: latitude
        in: path
        type: number
        format: float
        required: true
        description: The decimal latitude of the area to retrieve measurements for.
      - name: longitude
        in: path
        type: number
        format: float
        required: true
        description: The decimal longitude of the area to retrieve measurements for.
      - name: radius
        in: path
        type: number
        format: float
        required: true
        description: The radius (km) around the given coordinates to retrieve measurements for.
    responses:
      200:
        description: A list of measurements for the given pollutant in the specified area.
        schema:
          type: array
          items:
            $ref: '#/definitions/Measurement'
      404:
        description: No measurements found for this area.
    """
    service = MeasurementService()

    entities = service.retrieve_by_area(
        pollutant=pollutant,
        latitude=float(latitude),
        longitude=float(longitude),
        radius=float(radius),
    )

    if not entities:
        return jsonify({"message": "No measurements found for this area."}), 404

    return jsonify([vars(entity) for entity in entities]), 200
