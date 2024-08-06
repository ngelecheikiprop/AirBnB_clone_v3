#!/usr/bin/python3
"""States apis
"""
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify

@app_views.route('/states', strict_slashes = False)
def get_states():
    """gets all states
    """
    my_dict = {}
    for key, value in storage.all(State).items():
        my_dict[key] = value.to_dict()
    return jsonify(my_dict)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def get_a_state(state_id):
    """get a state with id given
    """
    return jsonify(storage.get(State, state_id).to_dict())


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['DELETE'])
def del_a_state(state_id):
    """deletes a state of given id
    """
    storage.delete(storage.get(State, state_id))
    return jsonify({})
