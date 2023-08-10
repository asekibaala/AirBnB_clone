#!/usr/bin/python3
"""This module defines BaseModel claass which hold common attributes
that will be used but several instances of the class"""
import uuid
from datetime import datetime

class BaseModel():
    """Defines common attributes that will be used in other
    instances.
    """
    def __init__(self):
        """initializes class"""
        self.id = str(uuid.uuid4)
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
            
        
    
    def __str__(self):
        """string representation of base model"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )
            
    def save(self):
        self.updated_at = datetime.now().isoformat()
        
    
    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at
        dictionary['updated_at'] = self.updated_at
        return dictionary