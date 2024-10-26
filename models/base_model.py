#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone."""

import uuid
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models."""

    id = Column(String(128), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.now(timezone.utc))

    def __init__(self, *args, **kwargs):
        """Instantiates a new model."""
        if not kwargs:
            # print("DEBUG: NOT KWARGS")  # DEBUG
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)
        else:
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.fromisoformat(
                    kwargs['updated_at'])
            else:
                self.updated_at = datetime.now(timezone.utc)
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.fromisoformat(
                    kwargs['created_at'])
            else:
                self.created_at = datetime.now(timezone.utc)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if '__class__' in kwargs:
                del kwargs['__class__']
            # print('DEBUG: BaseModel Else')  # DEBUG
            for key, val in kwargs.items():
                # print('DEBUG: BaseModel: {}'.format(key))  # DEBUG
                if key not in ['updated_at','created_at']:
                    setattr(self, key, val)
                    # print('DEBUG: setattr')  # DEBUG
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance."""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed."""
        from models import storage
        self.updated_at = datetime.now(timezone.utc)
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format."""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({
            '__class__': (str(type(self)).split('.')[-1]).split('\'')[0]
        })
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes a BaseModel instance from models.storage."""
        from models import storage
        storage.delete(self)
