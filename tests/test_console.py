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
import uuid
from time import sleep


class Test_console(unittest.TestCase):
    """Test cases for the console.py file
    """
    clis = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'Review', 'State']
    storage = FileStorage()

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
        _help = 'Quit method to exit form cmd '
        _help += 'program (Usage: quit)\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), _help)

    def test_help_EOF(self):
        """Test for help EOF command
        """
        _help = 'EOF method to exit cmd program\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), _help)

    def test_help_all(self):
        """Test for help all command
        """
        _help = "[Usage: all <class name>]or [Usage: all] or "\
                "[Usage: <class name>.all()]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue(), _help)

    def test_help_count(self):
        """Test for help count command
        """
        _help = "[Usage: <class name>.count()]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(f.getvalue(), _help)

    def test_help_create(self):
        """Test for help create command
        """
        _help = "[Usage: create <class name>]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue(), _help)

    def test_help_destroy(self):
        """Test for help EOF command
        """
        _help = "[Usage: destroy <class name> <id>] or "\
                "[Usage: <class name>.destroy(<id>)]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue(), _help)

    def test_help_show(self):
        """Test for help show command
        """
        _help = "[Usage: show <class name> <id>] or "\
                "[Usage: <class name>.show(<id>)]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue(), _help)

    def test_help_update(self):
        """Test for help update command
        """
        _help = "[Usage: update <class name> <id> <attribute name> "\
                '"<attribute value>"] or [Usage: <class name>.update(<id>,'\
                "<attribute name>, <attribute value>)]\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue(), _help)

    def test_help_no_command(self):
        """Test for help a command that doesnt exist
        """
        _help = "*** No help on hello\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help hello")
            self.assertEqual(f.getvalue(), _help)

    def test_create(self):
        """Test for create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create hello")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")
            for _class in self.clis:
                with patch('sys.stdout', new=StringIO()) as f:
                    command = "create" + " " + _class
                    HBNBCommand().onecmd(command)
                    _id = f.getvalue().strip()
                    key = _class + "." + _id
                    self.assertTrue(key in storage.all().keys())

    def test_unknown(self):
        """ Command that does not exist """
        msg = "*** Unknown syntax: asd\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("asd")
            st = f.getvalue()
            self.assertEqual(msg, st)
