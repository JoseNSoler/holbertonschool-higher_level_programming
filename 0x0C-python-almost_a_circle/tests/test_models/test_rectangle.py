#!/usr/bin/python3

'''
Unittests for module base.py

'''

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    '''Unittests class module '''

    def test_rectangle_is_base(self):
        '''Is instance of base'''
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_two_args(self):
        '''id check for two objects - two arguments'''
        r1 = Rectangle(3, 9)
        r2 = Rectangle(9, 3)
        self.assertEqual(r1.id, 2)

    def test_two_args(self):
        '''id check for two objects - four arguments '''
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r1.id, 2)

    def test_err_no_args(self):
        '''>Error -- No arguments '''
        with self.assertRaises(TypeError):
            Rectangle()

    def test_err_one_arg(self):
        '''>Error -- Only one arg '''
        with self.assertRaises(TypeError):
            Rectangle(1)
    
    def test_width_private(self):
        '''>Error -- Access via private modifier '''
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 6).__width)


if __name__ == "__main__":
    unittest.main()