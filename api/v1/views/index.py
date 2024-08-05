from api.v1.views import app_views
from flask import jsonify
@app_views.route('/status')
def status():
    from flask import jsonify
    return jsonify({"status":"ok"})


@app_views.route('/stats')
def stats():
    from models import storage
    from models.amenity import Amenity
    from models.state import State
    from models.review import Review
    from models.city import City
    from models.user import User
    from models.place import Place
    mystats = {}
    mystats["amenities"] = storage.count(Amenity)
    mystats["cities"] = storage.count(City)
    mystats["places"] = storage.count(Place)
    mystats["reviews"] = storage.count(Review)
    mystats["states"] = storage.count(State)
    mystats["users"] = storage.count(User)
    return jsonify(mystats)
