#!/usr/bin/python3
"""defines a class to manage file storage for hbnb project"""

import os
import json
from importlib import import_module


class FileStorage:
    """manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initializes a FileStorage instance"""
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            filter_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    filter_dict[key] = value
            return filter_dict

    def delete(self, obj=None):
        """Removes an object from the storage dictionary"""
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        )

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as file:
            tmp = {}
            for key, val in self.__objects.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, file)

    def reload(self):
        """reLoads storage dictionary from file"""
        classes = self.model_classes
        if os.path.isfile(self.__file_path):
            temp = {}
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)

    def close(self):
        """Closes the storage engine."""
        self.reload()