from src import app

from flask import jsonify


@app.route("/health")
def health():
    """
    ---
    tags:
      - Health
    responses:
      200:
        description: The status of the health check.
        schema:
          type: string
    """
    return jsonify("healthy!"), 200
