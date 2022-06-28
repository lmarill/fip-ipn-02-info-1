from argparse import ArgumentTypeError
import sys, os

SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/..")
sys.path.append(SCRIPT_DIR)

import unittest
from modules.enums import EIngredient
from modules.ingredient import Ingredient

class TestingIngredient(unittest.TestCase):
    
    def test_constructor_nominal(self):
        ing = Ingredient(EIngredient.Apple)
        self.assertEqual(ing._type, EIngredient.Apple)
        self.assertEqual(ing.name, EIngredient.Apple.name)

    def test_constructor_argtypeerror(self):
        self.assertRaises(ArgumentTypeError, Ingredient, "Banana")
        self.assertRaises(ArgumentTypeError, Ingredient, 1)
        self.assertRaises(ArgumentTypeError, Ingredient, { "name": "Banana"})
        self.assertRaises(ArgumentTypeError, Ingredient, ["Banana"])

if __name__ == '__main__':
    unittest.main()