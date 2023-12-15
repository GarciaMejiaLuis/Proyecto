from . import db
#from flask_login import UserMixin


#userMix
class Persona(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    email=db.Column(db.String(100))

class Viaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dias = db.Column(db.Integer)
    fecha_inicio = db.Column(db.Date)
    fecha_regreso = db.Column(db.Date)
    precio = db.Column(db.Float)
    fecha_salida2 = db.Column(db.Date)
    fecha_regreso2 = db.Column(db.Date)