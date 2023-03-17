# flask, flask_googlemaps, flask_restful
from flask import Flask, render_template, request, redirect, url_for
from flask_googlemaps import GoogleMaps
from flask_restful import Resource, Api


app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = '611638969896-d57uu9m81bgbak25hha661uh8o4hnv2t.apps.googleusercontent.com'
GoogleMaps(app)
api = Api(app)

puntos_importantes = [
            {'name': 'Base de CBVCDE', 'lat':-25.535382 , 'lng':-54.633344 },
            {'name': 'Base de CBVCDE', 'lat':-25.535382 , 'lng':-54.633444 },
            {'name': 'Base de CBVCDE', 'lat':-25.535382 , 'lng':-54.633544 }
        ]

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
        return redirect(url_for('index'))
    return render_template('agregar.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000, debug = True)