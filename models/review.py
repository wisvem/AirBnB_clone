#!/usr/bin/python3
"""Module review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that defines Review attributes
    """
    place_id = ""
    user_id = ""
    text = ""
