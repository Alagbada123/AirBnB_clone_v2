#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, ForeignKey, String
from . import engine


class State(BaseModel):
    """ State class """
    # if  engine.storage_type == 'db':
    #     __tablename__ = 'states'
    #     name = Column(String(128), nullable=False)

    # else:
    #     name = ''
    name = ''
