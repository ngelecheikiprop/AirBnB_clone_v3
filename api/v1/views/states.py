#!/usr/bin/python3
"""States apis
"""
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify,abort

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


@app_views.route('/states',strict_slashes=False)
def post_a_state():
    """creates a state
    """
    newState = State()
    
