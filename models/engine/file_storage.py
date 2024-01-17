#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls != None:
            return {key: obj for key, obj in FileStorage.__objects.items() if isinstance(obj, cls)}
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

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
                    class_name = val['_class_']
                    if class_name in classes:
                        class_obj = classes[class_name]
                        del val['_class']  # Remove the __class_ key from the dictionary
                        self.all()[key] = class_obj(**val)
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error reloading objects: {}".format(e))

    def delete(self, obj=None):
        """ Deletes obj from __objects if it is available"""
        if obj != None:
            #key = obj.to_dict()['__class__'] + '.' + obj.id
            key = "{}.{}".format(type(obj).__name__, obj.id)
            #self.all().pop(key, None)
            del self.__objects[key]
