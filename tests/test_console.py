#!/usr/bin/python3
"""Console unittest
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage
from models.engine.file_storage import FileStorage
import inspect
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class Test_console(unittest.TestCase):
    """Test cases for the console.py file
    """
    clis = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'Review', 'State']

    def setUp(self):
        """set environment to start testing"""
        # Empty objects in engine
        FileStorage._FileStorage__objects = {}
        # Remove file.json if exists
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """set enviroment when testing is finished"""
        # Empty objects in engine
        FileStorage._FileStorage__objects = {}
        # Remove file.json if exists
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_help_quit(self):
        """Test for help quit command
        """
        help_quit = 'Quit method to exit form cmd '
        help_quit += 'program (Usage: quit)\n        \n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), help_quit)

    def test_help_EOF(self):
        """Test for help EOF command
        """
        help_EOF = 'EOF method to exit cmd program\n        \n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), help_EOF)
