#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from os import geten
import models
import os

    
class State(BaseModel, Base):
    """ State class """
    
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        cities =relationship("City", backref="state", cascade="all, delete-orphan")

    else:

        class State(BaseModel):
            """ File storage State """
        name = ""
    
        @property
        def cities(self):
            """ Returns list of City instances with state id = to the current State id"""
        
            list_cities = []
            for key, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    list_cities.append(city)
                return list_cities