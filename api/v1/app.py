#!/usr/bin/python3
"""
main routh engine
doc
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flasgger import Swagger
from flask_cors import CORS, cross_origin

app = Flask(__name__)

host = getenv("HBNB_API_HOST", "0.0.0.0")
port = getenv("HBNB_API_PORT", "5000")

"swagger = Swagger(app)"
cors = CORS(app, resources={r'/*': {'origins': host}})

app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """
    clean up
    """
    storage.close()


@app.errorhandler(404)
def my_44(err_msg):
    """
    not found
    """
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    app.run(debug=True, port=port, host=host, threaded=True)
