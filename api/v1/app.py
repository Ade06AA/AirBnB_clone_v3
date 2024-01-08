#!/usr/bin/python3
"""
main routh engine
"""

from flask import Flask
from models import storage
from api.v1.viewsimport import app_views
from os import getenv

app = Flask(__name__)

@app.teardown_appcontext
def teardown():
    """
    clean up
    """
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(debug=True, port=port, host=host, threaded=True)
