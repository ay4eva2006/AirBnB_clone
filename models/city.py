#!/usr/bin/python3
import models
from models.base_model import BaseModel


class City(BaseModel):
    '''City class inherit from BaseModel class
    '''
    state_id = ""
    name = ""
