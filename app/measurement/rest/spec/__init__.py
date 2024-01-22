definitions = {
    "Measurement": {
        "type": "object",
        "properties": {
            "id_": {"type": "string", "description": "The id of the measurement"},
            "created_at": {
                "type": "string",
                "format": "date-time",
                "description": "The time when the measurement was created",
            },
            "updated_at": {
                "type": "string",
                "format": "date-time",
                "description": "The time when the measurement was last updated",
            },
            "archived": {
                "type": "boolean",
                "description": "Whether the measurement is archived",
            },
            "recorded_at": {
                "type": "string",
                "format": "date-time",
                "description": "The time when the measurement was recorded",
            },
            "city": {
                "type": "string",
                "description": "The city where the measurement was taken",
            },
            "country": {
                "type": "string",
                "description": "The country where the measurement was taken",
            },
            "latitude": {
                "type": "number",
                "format": "float",
                "description": "The latitude where the measurement was taken",
            },
            "longitude": {
                "type": "number",
                "format": "float",
                "description": "The longitude where the measurement was taken",
            },
            "pollutant": {
                "type": "string",
                "description": "The pollutant that the measurement is for",
            },
            "value": {
                "type": "number",
                "format": "float",
                "description": "The value of the measurement",
            },
        },
    }
}
