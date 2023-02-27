from flask import Blueprint, jsonify, abort, request
from ..models import User, Allergie, db

bp = Blueprint('user',__name__, url_prefix='/user')


#creates a new user
@bp.route('/register', methods=['POST'])
def register_user():
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)
    u = User(username = request.json['username'], password = request.json['password'])
    db.session.add(u)
    db.session.commit()
    return f"succesfully created {u.__repr__()} account."

#registers an allergie to the system
@bp.route('/register_allergie', methods=['POST'])
def register_allergie():
    for value in request.json.values():
        a = Allergie(allergie=value)
        db.session.add(a)
    db.session.commit()
    
    return "Allergies have been resitered"