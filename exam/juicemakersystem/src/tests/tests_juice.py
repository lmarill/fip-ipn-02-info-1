from argparse import ArgumentTypeError
import sys, os

SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/..")
sys.path.append(SCRIPT_DIR)

import unittest

from modules.juice import Juice, TheBoost, TheFresh, TheDetox, TheFusion
from modules.ingredient import Ingredient
from modules.enums import EIngredient, ESize

class TestingJuice(unittest.TestCase):
    
    def test_constructor_nominal(self):
        juice = Juice("MyFirstJuice", ESize.Small, 15, {})
        self.assertEqual(juice.name, "MyFirstJuice")
        self.assertEqual(juice.size, ESize.Small)
        self.assertEqual(juice.price, 15)
        self.assertEqual(juice.recipe, {})

        recipe = {
            Ingredient(EIngredient.Apple): 1,
            Ingredient(EIngredient.Banana): 2
        }
        juice = Juice("MyFirstJuice", ESize.Small, 15, recipe)
        self.assertEqual(juice.name, "MyFirstJuice")
        self.assertEqual(juice.size, ESize.Small)
        self.assertEqual(juice.price, 15)
        self.assertEqual(juice.recipe, recipe)

    def test_constructor_argtypeerror(self):
        self.assertRaises(ArgumentTypeError, Juice, 10, ESize.Large, 10, {})
        self.assertRaises(ArgumentTypeError, Juice, "testname", "Small", 10, {})
        self.assertRaises(ArgumentTypeError, Juice, "testname", ESize.Small, "10", {})
        self.assertRaises(ArgumentTypeError, Juice, "testname", ESize.Small, 10.5, "")
        self.assertRaises(ArgumentTypeError, Juice, "testname", ESize.Small, 10.5, {"Apple": 1, Ingredient(EIngredient.Banana): 2})
        self.assertRaises(ArgumentTypeError, Juice, "testname", ESize.Small, 10.5, {Ingredient(EIngredient.Apple): "1", Ingredient(EIngredient.Banana): 1})

    def test_price(self):
        recipe = {
            Ingredient(EIngredient.Apple): 1,
            Ingredient(EIngredient.Banana): 2
        }

        juice = Juice("MyJuice", ESize.Small, 15, recipe)
        self.assertEqual(juice.price, 15)

        juice = Juice("MyJuice", ESize.Medium, 15, recipe)
        self.assertEqual(juice.price, 15.5)

        juice = Juice("MyJuice", ESize.Large, 15, recipe)
        self.assertEqual(juice.price, 16)

class TestingTheBoost(unittest.TestCase):
    def test_recipe(self):
        expected = {
            Ingredient(EIngredient.Mango): 0.5,
            Ingredient(EIngredient.Orange): 2,
            Ingredient(EIngredient.Guajana): 1
        }

        juice = TheBoost()
        recipe = juice.recipe
        
        expected_keys = [ k.name for k in expected.keys() ]
        recipe_keys = [ k.name for k in recipe.keys() ]

        self.assertEqual(expected_keys, recipe_keys)

        for expected_key, expected_value in expected.items():
            for recipe_key, recipe_value in recipe.items():
                if expected_key.name == recipe_key.name:
                    self.assertEqual(expected_value, recipe_value)

class TestingTheFusion(unittest.TestCase):
    def test_recipe(self):
        expected = {
            Ingredient(EIngredient.Guava): 1,
            Ingredient(EIngredient.Pineapple): 0.25,
            Ingredient(EIngredient.Banana): 0.5
        }

        juice = TheFusion()
        recipe = juice.recipe
        
        expected_keys = [ k.name for k in expected.keys() ]
        recipe_keys = [ k.name for k in recipe.keys() ]

        self.assertEqual(expected_keys, recipe_keys)

        for expected_key, expected_value in expected.items():
            for recipe_key, recipe_value in recipe.items():
                if expected_key.name == recipe_key.name:
                    self.assertEqual(expected_value, recipe_value)

class TestingTheFresh(unittest.TestCase):
    def test_recipe(self):
        expected = {
            Ingredient(EIngredient.Apple): 3,
            Ingredient(EIngredient.Ginger): 1,
            Ingredient(EIngredient.Lemon): 1
        }

        juice = TheFresh()
        recipe = juice.recipe
        
        expected_keys = [ k.name for k in expected.keys() ]
        recipe_keys = [ k.name for k in recipe.keys() ]

        self.assertEqual(expected_keys, recipe_keys)

        for expected_key, expected_value in expected.items():
            for recipe_key, recipe_value in recipe.items():
                if expected_key.name == recipe_key.name:
                    self.assertEqual(expected_value, recipe_value)

class TestingTheDetox(unittest.TestCase):
    def test_recipe(self):
        expected = {
            Ingredient(EIngredient.Carrot): 3,
            Ingredient(EIngredient.CeleryStick): 1,
            Ingredient(EIngredient.Beetroot): 1
        }

        juice = TheDetox()
        recipe = juice.recipe
        
        expected_keys = [ k.name for k in expected.keys() ]
        recipe_keys = [ k.name for k in recipe.keys() ]

        self.assertEqual(expected_keys, recipe_keys)

        for expected_key, expected_value in expected.items():
            for recipe_key, recipe_value in recipe.items():
                if expected_key.name == recipe_key.name:
                    self.assertEqual(expected_value, recipe_value)


if __name__ == '__main__':
    unittest.main()
