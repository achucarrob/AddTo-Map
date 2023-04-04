from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# ########## MODELOS #########

#crear modelo para la base de datos: Mapas
class Mapas(db.Model):
    id_mapa = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    latitud = db.Column(db.Float())
    longitud = db.Column(db.Float())
    categoria = db.Column(db.String(50))