#!/usr/bin/python3
import models 
from models.base_model import BaseModel


class User(BaseModel):
    ''' user class that inherit 
       from BaseModel class
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
