from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'
    
    serialize_rules = ('-hero_powers.hero',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    hero_powers = db.relationship('HeroPower', backref = 'hero')
    
    def __repr__(self):
        return f'<The heroes name is {self.name} and his super name is {self.super_name}>'

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    
    serialize_rules = ('-hero_powers.power',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    hero_powers = db.relationship('HeroPower', backref = 'power')
    
    def __repr__(self):
        return f'<The power is named {self.name} and it {self.description}>'

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'
    
    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    
    def __repr__(self):
        return f'<The strength of the power is {self.strength}>'