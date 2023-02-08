#!/usr/bin/python3


import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Initialization of BaseModel class
       to create our attributes
       for the uuid4, created_at and updated_at
    """ 
    def __init__(self, *args, **kwargs):
        if len(kwargs) and kwargs != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "updated_at" or key == "created_at":
                        self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """This will display the BaseModel 
           with the user id and the dict
           of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ This will display the current datetime"""
        
        self.updated_at = datetime.now()

    def to_dict(self):
        """ This will return a dictionary 
            containing all keys/values of 
            __dict__ of the instance
        """
        temp_dict = dict(self.__dict__)
        temp_dict["__class__"] = self.__class__.__name__
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        return temp_dict
