#!/usr/bin/python3
<<<<<<< HEAD
import models 
=======
"""Defines the User class."""
>>>>>>> 65ebb2ce342fb51c90f51e7dc3db24bc85a66cfc
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    ''' user class that inherit 
       from BaseModel class
    '''
=======
    """Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

>>>>>>> 65ebb2ce342fb51c90f51e7dc3db24bc85a66cfc
    email = ""
    password = ""
    first_name = ""
    last_name = ""
