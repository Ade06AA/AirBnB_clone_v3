#!/usr/bin/python3
"""
empty doc
"""
from api.v1.views import app_views
from models import storage
from flask import request, abort, make_response, jsonify
from flasgger import Swagger, swag_from

State = storage.classes["State"]


@app_views.route("/states", methods=["GET", "POST"],
                 endpoint="states_no_id", strict_slashes=False)
@app_views.route("/states/<state_id>", methods=["GET", "DELETE", "PUT"],
                 endpoint="states_id", strict_slashes=False)
@swag_from('swag_files/states_no_id.yml', endpoint="states_no_id",
           methods=["GET", "POST"])
@swag_from('swag_files/states_id.yml', endpoint="states_id",
           methods=["GET", "PUT", "DELETE"])
def B_states(state_id=None):
    """
    the B stands for blue print
    ----
    def
    """
    container = ''
    if state_id:
        if f"State.{state_id}" in storage.all(State):
            obj = storage.get(State, state_id)
        else:
            abort(404)
    if request.method == "GET":
        if not state_id:
            obj = storage.all(State).values()
            return jsonify([o.to_dict() for o in obj])
        return jsonify(obj.to_dict())

    elif request.method == "POST":
        if not request.is_json:
            abort(400, "Not a JSON")
        content = request.get_json()
        if "name" not in content:
            abort(400, "Missing name")
        obj = State(**content)
        obj.save()
        res = make_response(obj.to_dict())
        # one of the way to specify status code
        res.status_code = 201
        # or
        # return (obj.to_dict(), 201)
        return jsonify(res)

    elif request.method == "PUT":
        not_allowed = ["id", "create_at", "updated_at"]
        if not request.is_json:
            abort(400, "Not a JSON")
        content = request.get_json()
        for i, j in content.items():
            if i not in not_allowed:
                setattr(obj, i, j)
        obj.save()
        return jsonify(obj.to_dict())

    elif request.method == "DELETE":
        storage.delete(obj)
        storage.save()
        return jsonify({})
    else:
        abort(404, "Not found")
