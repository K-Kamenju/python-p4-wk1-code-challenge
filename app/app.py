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

@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def powers_by_id(id):
    if request.method == 'GET':
        power = Power.query.get(id)

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

    elif request.method == 'PATCH':
        power = Power.query.get(id)

        if power:
            data = request.get_json()

            try:
                for attr in data:
                    setattr(power, attr, data[attr])

                # Validate the model before committing changes
                db.session.commit()

                power_data = {
                    "id": power.id,
                    "name": power.name,
                    "description": power.description
                }
                return make_response(jsonify(power_data), 200)

            except ValueError as e:
                # Catch validation error and include it in the response
                error_response = {"error": str(e)}
                return make_response(jsonify(error_response), 400)

        else:
            error_response = {"error": "Power not found"}
            return make_response(jsonify(error_response), 404)


if __name__ == '__main__':
    app.run(port=5555)
