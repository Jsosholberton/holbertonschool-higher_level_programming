#!/usr/bin/python3
"""Unittest for base, rectangle and square"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """"""

    def test_base(self):
        """"""
        b1 = Base(3)
        self.assertEqual(b1.id, 3)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base()
        self.assertEqual(b4.id, 3)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        b6 = Base(1)
        self.assertEqual(b6.id, 1)
        #Test for TypeError
        b1 = Base("Hi")
        self.assertEqual(b1.id, "Hi") #this need int
        
    def test_rectangle(self):
        r1 = Rectangle(2, 2, 1, 1)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.area(), 4)
        self.assertEqual(r1.display(), None)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertTrue(r1, "[Rectangle] (4) 2/2 - 1/1")
        r1.update(12, 1, 1, 1)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.area(), 1)
        self.assertTrue(r1, "[Rectangle] (12), 1/1 - 1/1")
        r1.update(id=100, width=3, height=2, x=2, y=3) #not import the orden
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertTrue(r1, "[Rectangle] (100), 3/2 - 2/3")
