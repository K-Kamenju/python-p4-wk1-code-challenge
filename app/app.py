#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    response_body = {
        "Hello": "Welcome to my Backend",
        "To Continue": "Enter a valid URL Route"
    }
    
    response = make_response(jsonify(response_body), 200)
    return response

@app.route('/heroes')
def heroes():
    
    heroes_list = [hero.to_dict() for hero in Hero.query.all()]
    return make_response(jsonify(heroes_list), 200)

@app.route('/heroes/<int:id>')
def heroes_by_id(id):
    
    hero_data = Hero.query.filter_by(id=id).first().to_dict()
    return make_response(jsonify(hero_data), 200)
 

if __name__ == '__main__':
    app.run(port=5555)
