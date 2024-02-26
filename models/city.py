#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = Column(str(60), Foreignkey('state.id'), nullable=False)
    name = Column(str(128), nullable=False)
    __tablename__ = cities
