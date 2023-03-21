#!/usr/bin/python3
"""New engine DbStorage"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


Class_name = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """Manage DB storage"""

    __engine = None
    __session = None

    def __init__(self):
        # call value in env
        user = os.getenv("HBNB_MYSQL_USER")
        pswd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        # create engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user,
                                              pswd,
                                              host,
                                              db_name),
                                      pool_pre_ping=True
                                      )

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session"""

        if not self.__session:
            self.reload()
            
        dict_objects = {}
        # class given
        if cls != None:
            for obj in self.__session.query(cls).all():
                dict_objects.update({'{}.{}'.
                                     format(type(cls).__name__, obj.id,): obj})
        else:
            for k, v in Class_name.items():
                for obj in self.__session.query(v):
                    dict_objects.update({'{}.{}'.
                                         format(type(obj).__name__, obj.id,): obj})
        return (dict_objects)

    def new(self, obj):
        """ add new object to the db session"""
        self.__session.add(obj)

    def save(self):
        """ save all change by commit in the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete object from current db session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create db table & session"""
        # create all table
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(session)()

    def close(self):
        """ close db"""
        self.__session.close()
