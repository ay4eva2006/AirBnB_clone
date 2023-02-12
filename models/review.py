#!/usr/bin/python3
<<<<<<< HEAD
import models
=======
"""Defines the Review class."""
>>>>>>> 65ebb2ce342fb51c90f51e7dc3db24bc85a66cfc
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    '''Review class inherit from BaseModel class
    '''
=======
    """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

>>>>>>> 65ebb2ce342fb51c90f51e7dc3db24bc85a66cfc
    place_id = ""
    user_id = ""
    text = ""
