#!/usr/bin/python3
"""This module defines BaseModel claass which hold common attributes
that will be used but several instances of the class"""
import uuid
from datetime import datetime
import json

class BaseModel():
    """Defines common attributes that will be used in other
    instances.
    """
    def __init__(self):
        """initializes class"""
        # if kwargs:
        #     for key, value in kwargs.items():
        #         if key == 'created_at' or key == 'updated_at':
        #             value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        #         if key != '__class__':
        #             setattr(self, key, value)
        # else:
        #     self.id = str(uuid.uuid4())
        #     self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        #     self.updated_at = self.created_at
        self.id = str(uuid.uuid4)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
            
        
    
    def __str__(self):
        """string representation of base model"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )
            
    def save(self):
        self.updated_at = datetime.now()
        # data = json.dumps(self.__dict__)
        # with open('data.json', 'w') as file:
        #     file.write(data)
    
    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary