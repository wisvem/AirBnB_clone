#!/usr/bin/python3
"""engine unittest
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


class Test_engine(unittest.TestCase):
    """Engine test class
    """
    clis = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'Review', 'State']

    def setUp(self):
        """set environment to start testing"""
        # Empty objects in engine
        from models.engine.file_storage import FileStorage
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

    def test_engine_000(self):
        """Test if all_obs is empty"""
        all_objs = storage.all()
        self.assertEqual(all_objs, {})

    def test_engine_001(self):
        """Test BaseModel object"""
        my_model = BaseModel()
        all_objs = storage.all()
        objid = None
        for objid in all_objs:
            pass
        mystr = my_model.__class__.__name__+'.'+my_model.id
        self.assertEqual(objid, mystr)
        # test full object
        objid = {mystr: my_model}
        self.assertEqual(all_objs, objid)

    def test_engine_002(self):
        """Test User object"""
        my_model = User()
        all_objs = storage.all()
        objid = None
        for objid in all_objs:
            pass
        mystr = my_model.__class__.__name__+'.'+my_model.id
        self.assertEqual(objid, mystr)
        # test full object
        objid = {mystr: my_model}
        self.assertEqual(all_objs, objid)

    def test_engine_003(self):
        """Test Place object"""
        my_model = User()
        all_objs = storage.all()
        objid = None
        for objid in all_objs:
            pass
        mystr = my_model.__class__.__name__+'.'+my_model.id
        self.assertEqual(objid, mystr)
        # test full object
        objid = {mystr: my_model}
        self.assertEqual(all_objs, objid)

    def test_engine_004(self):
        """Test City object"""
        my_model = City()
        all_objs = storage.all()
        objid = None
        for objid in all_objs:
            pass
        mystr = my_model.__class__.__name__+'.'+my_model.id
        self.assertEqual(objid, mystr)
        # test full object
        objid = {mystr: my_model}
        self.assertEqual(all_objs, objid)

    def test_engine_005(self):
        """Test Amenity object"""
        my_model = Amenity()
        all_objs = storage.all()
        objid = None
        for objid in all_objs:
            pass
        mystr = my_model.__class__.__name__+'.'+my_model.id
        self.assertEqual(objid, mystr)
        # test full object
        objid = {mystr: my_model}
        self.assertEqual(all_objs, objid)

    def test_engine_006(self):
        """Test Review object"""
        my_model = Review()
        all_objs = storage.all()
        objid = None
        for objid in all_objs:
            pass
        mystr = my_model.__class__.__name__+'.'+my_model.id
        self.assertEqual(objid, mystr)
        # test full object
        objid = {mystr: my_model}
        self.assertEqual(all_objs, objid)

    def test_engine_007(self):
        """Test State object"""
        my_model = State()
        all_objs = storage.all()
        objid = None
        for objid in all_objs:
            pass
        mystr = my_model.__class__.__name__+'.'+my_model.id
        self.assertEqual(objid, mystr)
        # test full object
        objid = {mystr: my_model}
        self.assertEqual(all_objs, objid)

    def test_engine_008(self):
        var = 'a'
        for i in self.clis:
            exec(var, "= eval(i)()")
            var = var + 1

    def test_engine_009(self):
        pass

    def test_engine_010(self):
        pass

    def test_engine_011(self):
        pass

    def test_engine_012(self):
        pass

    def test_engine_013(self):
        pass
