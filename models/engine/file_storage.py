"""This module defines a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel

class FileStorage:
    """serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    # private instance attributes
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Return the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """ 
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
        
    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)
        """
        json_data = {}
        for key, obj in self.__objects.items():
            json_data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_data, file)
            
    def relaod(self):
        """ Reloads data
            Deserializes the JSON file to __objects
            But only if the JSON file (__file_path) exists;
            otherwise, it does nothing.
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    # Create an instance of the class based on class_name
                    # set its attributes using the values from the dictionary
                    # then add it to __objects dictionary
                    nw_obj = eval(value['__class__'])(**value)
                    self.__objects[key] = nw_obj
        except FileNotFoundError:
            pass
                    