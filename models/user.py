#!/usr/bin/python3
"""Module user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that defines user attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
