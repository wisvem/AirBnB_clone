#!/usr/bin/python3
"""Console unittest
"""
import pep8
from unittest.mock import create_autospec, patch
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
from unittest.mock import patch, create_autospec
from io import StringIO
from console import HBNBCommand
import uuid
from time import sleep
import sys


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
            self.assertNotEqual(f.getvalue(), _help)

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
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("asd")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


classes = ["BaseModel", "User", "State", "City",
           "Amenity", "Place", "Review"]


class TestConsole00(unittest.TestCase):

    @classmethod
    def teardown(cls):
        """Final statement"""
        try:
            os.remove("file.json")
        except:
            pass

    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create_session(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_create(self):
        """Tesing create command"""
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('create'))
        self.assertEqual('** class name missing **',
                         Output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('create hola'))
        self.assertEqual("** class doesn't exist **",
                         Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
            self.assertEqual(36, len(Output.getvalue().strip()))

    def test_show(self):
        """Tests show command"""
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('show'))
        self.assertEqual('** class name missing **',
                         Output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('show hola'))
        self.assertEqual("** class doesn't exist **",
                         Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('show {}'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('show {} 123456'.format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('show {} {}'.format(cls, ids)))
            self.assertTrue(ids in Output.getvalue().strip())
            self.assertTrue(cls in Output.getvalue().strip())
            self.assertTrue("created_at" in Output.getvalue().strip())
            self.assertTrue("updated_at" in Output.getvalue().strip())

        """ <class>.show(<id>) method """

        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.show()'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.show("23456")'.format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.show("{}")'.format(cls, ids)))
            self.assertTrue(ids in Output.getvalue().strip())
            self.assertTrue(cls in Output.getvalue().strip())
            self.assertTrue("created_at" in Output.getvalue().strip())
            self.assertTrue("updated_at" in Output.getvalue().strip())

    def test_destroy(self):
        """Tests destroy command"""
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('destroy'))
        self.assertEqual('** class name missing **',
                         Output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('destroy hola'))
        self.assertEqual("** class doesn't exist **",
                         Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('destroy {}'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('destroy {} 123456'.format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('all'))
            self.assertTrue(ids in Output.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('destroy {} {}'.format(cls, ids)))
            self.assertFalse(ids in Output.getvalue().strip())
            self.assertEqual("", Output.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('all'))
            self.assertFalse(ids in Output.getvalue().strip())

        """ <class>.destroy(<id>) method """

        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.destroy()'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.destroy("123456")'
                                            .format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('all'))
            self.assertTrue(ids in Output.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.destroy("{}")'
                                            .format(cls, ids)))
            self.assertFalse(ids in Output.getvalue().strip())
            self.assertEqual("", Output.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('all'))
            self.assertFalse(ids in Output.getvalue().strip())

    def test_all(self):
        """Tests all command"""
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('all'))
        self.assertEqual('[', Output.getvalue().strip()[0])
        self.assertEqual(']', Output.getvalue().strip()[-1])
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('all hola'))
        self.assertEqual("** class doesn't exist **",
                         Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('all {}'.format(cls)))
                self.assertEqual('[', Output.getvalue().strip()[0])
                self.assertEqual(']', Output.getvalue().strip()[-1])
            self.assertTrue(ids in Output.getvalue().strip())

        """ <class>.all mode """

        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.all()'.format(cls)))
            self.assertEqual('[', Output.getvalue().strip()[0])
            self.assertEqual(']', Output.getvalue().strip()[-1])
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.all()'.format(cls)))
            self.assertTrue(ids in Output.getvalue().strip())

    def test_update(self):
        """Tests update command"""
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('update'))
        self.assertEqual('** class name missing **',
                         Output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('update hola'))
        self.assertEqual("** class doesn't exist **",
                         Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('update {}'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('update {} 123456'.format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('update {} {}'.format(cls, ids)))
            self.assertEqual("** attribute name missing **",
                             Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('update {} {} attribute'
                                            .format(cls, ids)))
            self.assertEqual("** value missing **", Output.getvalue().strip())
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('update {} {} attribute "test"'
                                            .format(cls, ids)))
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('show {} {}'.format(cls, ids)))
            self.assertTrue("attribute" in Output.getvalue().strip())
            self.assertTrue("test" in Output.getvalue().strip())

    def test_count(self):
        """Tests count command"""
        cli = self.create_session()
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.count()'.format(cls)))
                number1 = int(Output.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.count()'.format(cls)))
                number2 = int(Output.getvalue().strip())
            self.assertTrue(number2 == number1 + 1)

    def test_exit(self):
        """Tests exit command"""
        cli = self.create_session()
        self.assertTrue(cli.onecmd("quit"))
