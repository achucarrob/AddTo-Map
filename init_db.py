from models import db, Mapas
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask('app')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mapa.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# create tables
with app.app_context():
    db.create_all()

    db.session.commit()
    db.session.commit()
