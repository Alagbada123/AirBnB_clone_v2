#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """Returns the list of City instances."""
            list_city = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
