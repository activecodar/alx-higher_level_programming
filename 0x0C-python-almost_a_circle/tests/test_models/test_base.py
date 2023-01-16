#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init_with_id(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_init_with_id_is_int(self):
        b1 = Base(1)
        self.assertIsInstance(b1.id, int)

    def test_nb_objects_class_attribute(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)

if __name__ == '__main__':
    unittest.main()
