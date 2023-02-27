from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    patients = db.relationship('Patient', backref='users')

    def __repr__(self):
        return f'<User {self.username}>'
    
    
patient_biometric = db.Table(
    'patients_biometrics',
    db.Column('patient_id', db.Integer, db.ForeignKey('patients.id'), primary_key=True),
    db.Column('biometric_id', db.Integer, db.ForeignKey('biometrics.id'), primary_key=True)
)

patient_disliked_food = db.Table(
    'patients_disliked_foods',
    db.Column('patient_id', db.Integer, db.ForeignKey('patients.id'), primary_key=True),
    db.Column('disliked_food_id', db.Integer, db.ForeignKey('disliked_foods.id', primary_key=True))
)

patient_allergie = db.Table(
    'patients_allergies',
    db.Column('patient_id', db.Integer, db.ForeignKey('patients.id'), primary_key=True),
    db.Column('allergie_id', db.Integer, db.ForeignKey('allergies.id'), primary_key=True)
    )

class Patient(db.Model):
    __tablename__='patients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128))
    state = db.Column(db.String(128))
    goal = db.relationship('Goal', backref='patients', uselist=False)
    biometrics = db.relationship('Biometric', secondary = patient_biometric, backref= 'patients')
    disliked_foods = db.relationship('Disliked_food', secondary= patient_disliked_food, backref='patients')
    allergies = db.relationship('Allergie', secondary = patient_allergie, backref='patients')

    def get_patient_info(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'country': self.country,
            'state': self.state,
            'goal': self.goal,
            'biometrics': self.biometrics,
            'disliked_foods': self.disliked_foods,
            'allergies': self.allergies
        }

class Allergie(db.Model):
    __tablename__='allergies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    allergie = db.Column(db.String(128), nullable=False)

class Biometric(db.Model):
    __tablename__="biometrics"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    gender = db.Column(db.Float)
    waist = db.Column(db.Float)
    chest = db.Column(db.Float)
    hip = db.Column(db.Float)
    bim = db.Column(db.Float)
    body_fat = db.Column(db.Float)
    fat_free_mass = db.Column(db.Float)

class Disliked_food(db.Model):
    __tablename__="disliked_foods"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food = db.Column(db.String(128), nullable=False)

class Goal(db.Model):
    __tablename__= "goals"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Float)
    bmi = db.Column(db.Float)
    body_fat = db.Column(db.Float)
    fat_free_mass = db.Column(db.Float)











