#!/usr/bin/python3
"""This module defines BaseModel claass which hold common attributes
that will be used but several instances of the class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines common attributes that will be used in other
    instances.
    """

    def __init__(self, *args, **kwargs):
        """initializes class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string representation of base model"""
        return (
            "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        )

    # def __repr__(self):
    #     """returns string"""
    #     return self.__str__

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
