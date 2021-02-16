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
        my_model = Place()
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
        """ Save method with base model """
        filename = "file.json"
        mymodel = BaseModel()
        key = mymodel.__class__.__name__+'.'+mymodel.id
        self.assertFalse(os.path.exists(filename))
        storage.new(mymodel)
        storage.save()
        self.assertTrue(os.path.exists(filename))
        with open(filename) as f:
            myobj = json.load(f)
            self.assertEqual(mymodel.id, myobj[key]["id"])
            self.assertEqual(mymodel.__class__.__name__,
                             myobj[key]["__class__"])

    def test_engine_009(self):
        """Test reload function"""
        filename = "file.json"
        mymodel = BaseModel()
        my_obj = mymodel.__class__.__name__ + '.'+mymodel.id
        self.assertFalse(os.path.exists(filename))
        self.assertTrue(len(storage.all()) == 1)
        storage.save()
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(len(storage.all()) == 1)
        # Empty the __objects to check if reload works
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        self.assertTrue(len(storage.all()) == 0)
        storage.reload()
        all_obj = storage.all()
        self.assertFalse(mymodel == all_obj[my_obj])
        self.assertEqual(mymodel.id, all_obj[my_obj].id)
        self.assertEqual(mymodel.__class__, all_obj[my_obj].__class__)
        self.assertEqual(mymodel.created_at, all_obj[my_obj].created_at)
        self.assertEqual(mymodel.updated_at, all_obj[my_obj].updated_at)
        self.assertTrue(len(storage.all()) == 1)

    def test_engine_010(self):
        """Test reload whit all classes"""
        filename = "file.json"
        baseobj = BaseModel()
        userobj = User()
        cityobj = City()
        ameobj = Amenity()
        placeobj = Place()
        reviewobj = Review()
        stateobj = State()
        id1 = baseobj.__class__.__name__ + '.' + baseobj.id
        id2 = userobj.__class__.__name__ + '.' + userobj.id
        id3 = cityobj.__class__.__name__ + '.' + cityobj.id
        id4 = ameobj.__class__.__name__ + '.' + ameobj.id
        id5 = placeobj.__class__.__name__ + '.' + placeobj.id
        id6 = reviewobj.__class__.__name__ + '.' + reviewobj.id
        id7 = stateobj.__class__.__name__ + '.' + stateobj.id
        self.assertFalse(os.path.exists(filename))
        storage.save()
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        clist = [baseobj, userobj, cityobj,
                 ameobj, placeobj, reviewobj, stateobj]
        for i, j in zip(clist, range(1, 7)):
            ids = "id" + str(j)
            self.assertFalse(i == alldic[eval(ids)])
            self.assertEqual(i.id, alldic[eval(ids)].id)
            self.assertEqual(i.__class__, alldic[eval(ids)].__class__)

    def test_engine_011(self):
        """Test storage new"""
        mymodel = BaseModel()
        objid = mymodel.__class__.__name__ + '.'+mymodel.id
#       self.assertEqual(allobjs, {})
        allobjs = storage.all()
        storage.new(mymodel)
        allobjs = storage.all()
        self.assertEqual(mymodel, allobjs[objid])

    def test_engine_012(self):
        """Test creation with a dict"""
        userdic = {'id': "Wiston"}
        mymodel = User(**userdic)
        objid = mymodel.__class__.__name__ + '.'+mymodel.id
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(all_objs, {})
        storage.new(mymodel)
        all_objs = storage.all()
        self.assertEqual(mymodel, all_objs[objid])

    def test_engine_013(self):
        """ Test empty file"""
        filename = "file.json"
        self.assertFalse(os.path.exists(filename))
        storage.reload()

    def test_engine_014(self):
        """Instance of storage class"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_engine015(self):
        """File storage class atributes"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def tool_engine_016(self, classname):
        """helper func for save tests"""
        mycls = storage.classes()[classname]
        obj = mycls()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        mydic = {key: obj.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(mydic)))
            f.seek(0)
            self.assertEqual(json.load(f), mydic)
