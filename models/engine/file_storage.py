#!/usr/bin/python3
""" File Storage Module """
import json
from models.base_model import BaseModel


class FileStorage:
    """ Serializes instances to a JSON file and deserializes JSON
    file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns the list of objects of one type of class, 
        if the class specified, return objects in class"""
        if cls is None:
            return FileStorage.__objects
        dir_same_cls = {}
        for key, value in FileStorage.__objects.items():
            if value.__class__ == cls:
                dir_same_cls[key] = value
            return dir_same_cls

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

      def delete(self, obj=None):
        """ Deletes obj from __objects if it exists """
        if obj is not None:
            return
        
        key = obj.to_dict()['__class__'] + ''.' + obj.id
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]


    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """Deserializes JSON to objects"""
        self.reload()
