#!/usr/bin/python3
"""
main routh engine
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """
    clean up
    """
    storage.close()


@app.errorhandler(404)
def teardown(err_msg):
    """
    not found
    """
    return {"error": "Not found"}


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(debug=True, port=port, host=host, threaded=True)
