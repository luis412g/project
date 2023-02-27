from flask import Blueprint, jsonify, abort, request
from ..models import Patient, db

bp = Blueprint('patient',__name__, url_prefix='/patient')


#creates new patient
@bp.route('/register', methods=['POST'])
def create_patient():

    patient = Patient(
        user_id = request.json['user_id'],
        first_name = request.json['first_name'],
        last_name = request.json['last_name'],
        phone_number = request.json['phone_number'],
        email = request.json['email'],
        country = request.json['country'],
        state = request.json['state']
        )
    
    db.session.add(patient)
    db.session.commit()
    return jsonify(patient.get_patient_info())

#gets patient information
@bp.route('/<int:id>', methods=['GET'])
def get_patient_info(id: int):
    patient = Patient.query.get_or_404(id)
    return jsonify(patient.get_patient_info())

