#!/usr/bin/python3
"""Unittest for base, rectangle and square"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test for all the the objects"""

    def test_base(self):
        """Test for the base of the objects"""
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
        self.assertEqual(r1.area(), 6)
        self.assertTrue(r1, "[Rectangle] (100), 3/2 - 2/3")

    def test_square(self):
        """"""
        s1 = Square(3)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.area(), 9)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertTrue(s1, "[Rectangle] (6), 3/3 - 3")

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.area(), 4)
        self.assertTrue(s1, "[Rectangle] (1), 2/2 - 2")
        
        s1.update(size=3, id=5, x=1, y=1)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.area(), 9)
        self.assertTrue(s1, "[Rectangle] (5), 3/3 - 3")
