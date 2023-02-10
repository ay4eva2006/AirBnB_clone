#!/usr/bin/python3
import models
from models.base_model import BaseModel


class Review(BaseModel):
    '''Review class inherit from BaseModel class
    '''
    place_id = ""
    user_id = ""
    text = ""
