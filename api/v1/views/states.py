#!/usr/bin/python3
"""States apis
"""
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify, abort, request

@app_views.route('/states', strict_slashes=False, methods=['GET'])
def get_states():
    """gets all states
    """
    my_states = []
    for key, value in storage.all(State).items():
        my_states.append(value.to_dict())
    return jsonify(my_states)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def get_a_state(state_id):
    """get a state with id given
    """
    if not storage.get(State, state_id):
        abort(404)
    return jsonify(storage.get(State, state_id).to_dict())


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['DELETE'])
def del_a_state(state_id):
    """deletes a state of given id
    """
    if not storage.get(State, state_id):
        abort(404)
    storage.delete(storage.get(State, state_id))
    storage.save()
    return jsonify({}), 200


@app_views.route('/states',strict_slashes=False, methods=['POST'])
def post_a_state():
    """creates a state
    """
    if not request.json:
        abort(400,description="Not a JSON")
    if not 'name'in request.json:
        abort(400, description="Missing name")

    kwargs =request.get_json()
    new_state = State(**kwargs)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('states/<state_id>',strict_slashes=False, methods=['PUT'])
def update_a_state(state_id):
    """updates a state
    """
    if not storage.get(State, state_id):
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    my_state = storage.get(State, state_id)
    for key, value in request.get_json().items():
        if key == 'id' or key == 'created_at' or key == 'updated_at':
            continue
        my_state.key = value
    my_state.save()
    return jsonify(my_state.to_dict()), 200
