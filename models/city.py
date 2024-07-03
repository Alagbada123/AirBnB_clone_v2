#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import HBNB_TYPE_STORAGE

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    # for database storage
    if HBNB_TYPE_STORAGE == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    # for json file storage
    else:
        state_id = ""
        name = ""
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
