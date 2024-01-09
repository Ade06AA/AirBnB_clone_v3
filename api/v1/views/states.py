#!/usr/bin/python3
"""
empty doc
"""
from api.v1.views import app_views
from models import storage
from flask import request, abort, make_response

State = storage.classes["State"]


@app_views.route("/states", methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/states/<state_id>", methods=["GET", "DELETE", "PUT"],
                 strict_slashes=False)
def B_states(state_id=None):
    """
    the B stands for blue print
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
            return [o.to_dict() for o in obj]
        return obj.to_dict()

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
        return res

    elif request.method == "PUT":
        not_allowed = ["id", "create_at", "updated_at"]
        if not request.is_json:
            abort(400, "Not a JSON")
        content = request.get_json()
        for i, j in content.items():
            if i not in not_allowed:
                setattr(obj, i, j)
        obj.save()
        return obj.to_dict()

    elif request.method == "DELETE":
        storage.delete(obj)
        storage.save()
        return {}
    else:
        pass
