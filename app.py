
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_googlemaps import GoogleMaps
from flask_restful import Resource, Api
from models import db, Mapas
import json



app = Flask(__name__)
# Configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mapa.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
# Config API
app.config['GOOGLEMAPS_KEY'] = '611638969896-d57uu9m81bgbak25hha661uh8o4hnv2t.apps.googleusercontent.com'
GoogleMaps(app)
api = Api(app)

db.init_app(app)

puntos_importantes = []

class Puntos (Resource):
     def get(self):
         return puntos_importantes
api.add_resource(Puntos, '/api/puntos')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        lat = request.form['latitud']
        lng = request.form['longitud']
        nombre = request.form['nombre']

        puntos_importantes.append(
            {'name': nombre, 'lat': lat, 'lng': lng}
        )
        datos = Mapas(
            nombre = nombre,
            latitud = lat,
            longitud = lng,
            categoria = 'prueba'
        )
        db.session.add(datos)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('agregar.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1080, debug = True)