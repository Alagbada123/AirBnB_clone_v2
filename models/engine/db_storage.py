#!/usr/bin/python3
""" This module creates an engine for saving to database """
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

""" Setting env variables """
HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
HBNB_ENV = os.getenv('HBNB_ENV')


class DBStorage:
        """ Class to run database engine """
        __engine = None
        __session = None

        def __init__(self):
                """ Initializes class """
                self.__engine = create_engine(
                        'mysql+mysqldb://{}:{}@{}/{}'.format(
                                HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                        pool_pre_ping=True)

                # Drop all tables if env is test
                if HBNB_ENV == 'test':
                        drop_all(self.__engine)
                
        def all(self, cls=None):
                """ query on the current database session (self.__session) all objects depending of the class name (argument cls); returns dict """
                printf("In all")
                Session = sessionmaker(bind=self.__engine)
                session = Session()
                if cls == None:
                        # equal to show all?
                        for instance in session:
                                print("{}: {}".format(instance.id, instance.name))
                else:
                        print("Not set up yet")
                        # query based on cls

