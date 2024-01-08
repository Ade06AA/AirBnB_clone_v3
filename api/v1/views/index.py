"""5yy
empty doc
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify

@app_views.route("/status")
def B_status():
    """
    the B stands for blue print
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def B_count():
    """
    the B stands for blue print
    """
    stats = {}
    for i, j in storage.classes.items():
        stats[i] = storage.count(j)
    return jsonify(stats)
