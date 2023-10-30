#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from os import getenv


class DBStorage(self):
    self.__engine = None
    self.__session = None

    def __init__(self):
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}'
                                      f'@{host}/{database}',
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}
        classes = [States, City, User, Amenity, Place, Review]

        if cls is None:
            for class_name in classes:
                objects.update({obj.__class__.__name__ + '.' + obj.id: obj
                                for obj in self.__session.query(class_name).all()})

        else:
            if cls in classes:
                objects = {obj.__class__.__name__ + '.' + obj.id: obj
                           for obj in self.__session.query(cls).all()}

        return objects

        def new(self, obj):
            return self.__session.add(obj)

        def save(self):
            return self.__session.commit(obj)

        def delete(self, obj=None):
            if obj is not None:
                self.__session.delete(obj)

        def reload(self):
            Base.metadata.create_all(self.__engine)
            Session = scoped_session(sessionmaker(bind=self.__engine,
                                                  expire_on_commit=False))
