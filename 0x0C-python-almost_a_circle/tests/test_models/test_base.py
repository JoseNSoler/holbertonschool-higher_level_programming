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

    def test_args_id(self):
        '''arguments intervaling '''
        bas = Base()
        bas2 = Base()
        bas3 = Base()
        bas4 = Base(12)
        bas5 = Base()
        self.assertEqual(bas5.id, 4)

    def test_no_arg(self):
        '''No arguments '''
        b = Base()
        b2 = Base()
        self.assertEqual(6, b2.id)

    def test_id_public(self):
        '''Change id of object base '''
        base = Base(10)
        base.id = 5
        self.assertEqual(5, base.id)

    def test_id_inf(self):
        '''infinity test '''
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_str_arg(self):
        '''arguments by strings'''
        base_str = Base("20")
        self.assertEqual('20', base_str.id)

    def test_err_two_args(self):
        '''>Error -- two arguments '''
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
