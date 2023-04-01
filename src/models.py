import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Charecters(Base):
    __tablename__= 'charecters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    
    vehicle = Column(String(250), ForeignKey("vehicles.id"))
    birth_planet = Column(Integer(), ForeignKey("planets.id") )
    card_id = Column(Integer, ForeignKey("cards.id")) 

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    gravity = Column(Integer())
    diameter = Column(Integer())
    population = Column(Integer())
    climate = Column(String(250))
    terrain = Column(String(250))
    rotation_period = Column(Integer())
    orbital_period = Column(Integer())
    water_on_surface = Column(String(250))

    card_id = Column(Integer, ForeignKey("cards.id"))

class Vehicles(Base):
    __tablename__= 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    passengers = Column(Integer())
    cargo_capacity = Column(Integer())
    lenght = Column(String(250))
    max_atmosphering_speed = Column(Integer())

    card_id = Column(Integer, ForeignKey("cards.id"))

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    full_name = Column(String(250))
    date_suscription = Column(String(250))
    password = Column(Integer)
    email = Column(String(250))


class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    card_id = Column(Integer, ForeignKey("cards.id"))

    
class Cards(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
