import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
    
class User(Base):
    __tablename__ = 'user'
    user_id = Column(String, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    character_id = Column(Integer, ForeignKey('character.character_id'))
    planet_id = Column(Integer, ForeignKey('planet.planet_id'))
    user = relationship(User)
    character = relationship("Character")
    planet = relationship("Planets")

class Character(Base):
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True)
    character_name = Column(String(20))
    character_height = Column(Integer)
    character_mass = Column(Integer)
    character_gender = Column(String(20))
    character_films = Column(String(20))
    favorite_id = Column(Integer, ForeignKey('favorites.favorite_id'))
    favorites = relationship(Favorites)

class Planets(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(20))
    planet_diameter = Column(Integer)
    planet_climate = Column(String(20))
    planet_population = Column(Integer)
    planet_films = Column(String(20))
    favorite_id = Column(Integer, ForeignKey('favorites.favorite_id'))
    favorites = relationship(Favorites)

    def to_dict(self):
            return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')