#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()

class BaseModel:
    """A base class fo all hbnb models"""
    id = Column(String(128), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.now())  # utcnow deprecated
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.now())  # utcnow deprecated
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            print("DEBUG: NOT KWARGS")  # DEBUG
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)
        else:
            # if not in
            # else: create it for the above 3
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now(timezone.utc)
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now(timezone.utc)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if '__class__' in kwargs:
                del kwargs['__class__']
            print('DEBUG: BaseModel Else')  # DEBUG
            for key, val in kwargs.items():
                print('DEBUG: BaseModel: {}'.format(key))  # DEBUG
                if key not in ['updated_at','created_at']:
                    setattr(self, key, val)
                    print('DEBUG: setattr')  # DEBUG
            self.__dict__.update(kwargs)
            self.save()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """deletes a BaseModel Instance from models.storage"""
        from models import storage
        storage.delete(self)




# ORIGINAL CODE:
# class BaseModel:
#     """A base class for all hbnb models"""
#     def __init__(self, *args, **kwargs):
#         """Instatntiates a new model"""
#         if not kwargs:
#             from models import storage
#             self.id = str(uuid.uuid4())
#             self.created_at = datetime.now()
#             self.updated_at = datetime.now()
#             storage.new(self)
#         else:
#             kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
#                                                      '%Y-%m-%dT%H:%M:%S.%f')
#             kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
#                                                      '%Y-%m-%dT%H:%M:%S.%f')
#             del kwargs['__class__']
#             self.__dict__.update(kwargs)

#     def __str__(self):
#         """Returns a string representation of the instance"""
#         cls = (str(type(self)).split('.')[-1]).split('\'')[0]
#         return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

#     def save(self):
#         """Updates updated_at with current time when instance is changed"""
#         from models import storage
#         self.updated_at = datetime.now()
#         storage.save()

#     def to_dict(self):
#         """Convert instance into dict format"""
#         dictionary = {}
#         dictionary.update(self.__dict__)
#         dictionary.update({'__class__':
#                           (str(type(self)).split('.')[-1]).split('\'')[0]})
#         dictionary['created_at'] = self.created_at.isoformat()
#         dictionary['updated_at'] = self.updated_at.isoformat()
#         return dictionary
