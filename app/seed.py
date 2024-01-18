from app import app
from models import db, Hero, Power, HeroPower

from random import randint, choice as rc

from faker import Faker

fake = Faker()

with app.app_context():
    
    Hero.query.delete()
    Power.query.delete()
    HeroPower.query.delete()
    
    # Create heroes
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra")
    ]
    
    db.session.bulk_save_objects(heroes)
    db.session.commit()

    # Create powers
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths")
    ]
    
    db.session.bulk_save_objects(powers)
    db.session.commit()

    # Create HeroPower relationships
    hero_powers = [
        HeroPower(hero_id=randint(1, len(heroes)), power_id=randint(1, len(powers)), strength=rc(["Strong", "Weak", "Average"]))
        for _ in range(15)
    ]
    
    db.session.bulk_save_objects(hero_powers)
    db.session.commit()
