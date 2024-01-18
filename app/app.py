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
     
    hero = Hero.query.filter_by(id=id).first()

    if hero:
        hero_data = hero.to_dict()
        return make_response(jsonify(hero_data), 200)
    
    else:
        error_response = {"error": "Hero not found"}
        return make_response(jsonify(error_response), 404)
 
@app.route('/powers')
def powers():
    
    powers_list =[]
    for power in Power.query.all():
        power_data = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        powers_list.append(power_data)
    
    return make_response(jsonify(powers_list), 200)

@app.route('/powers/<int:id>')
def powers_by_id(id):
     
    power = Power.query.filter_by(id=id).first()

    if power:
        power_data = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        return make_response(jsonify(power_data), 200)
    
    else:
        error_response = {"error": "Power not found"}
        return make_response(jsonify(error_response), 404)

if __name__ == '__main__':
    app.run(port=5555)
