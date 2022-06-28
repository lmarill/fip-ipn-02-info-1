from argparse import ArgumentTypeError

import modules.enums as enums
import modules.ingredient as ingredient

class Juice():
    _name = ""
    _size = enums.ESize.Small
    _price = 0
    _recipe = {}

    def __init__(self, name, size, price, recipe):
        if not isinstance(name, str):
            raise ArgumentTypeError("name must be a string")

        if not isinstance(size, enums.ESize):
            raise ArgumentTypeError("size must be a enum")

        if not isinstance(price, (int, float)):
            raise ArgumentTypeError("price must be a number")

        if isinstance(recipe, dict):
            if not all(isinstance(k, ingredient.Ingredient) for k in recipe.keys()):
              raise ArgumentTypeError("keys must be an Ingredient")
            if not all(isinstance(v, (int, float)) for v in recipe.values()):
              raise ArgumentTypeError("keys must be a number")
        else:
            raise ArgumentTypeError("recipe must be a dict")

        self._name = name
        self._size = size
        self._price = price
        self._recipe = recipe
    
    def __repr__(self):
        return "%s for %s(%d$) is: %s" %(self.name, self.size.name, self.price, ', '.join(str((ingredient.name, value)) for ingredient, value in self._recipe.items()))

    @property
    def name(self): 
        return self._name 

    @property
    def size(self): 
        return self._size
    
    @property
    def price(self):
        if self.size == enums.ESize.Medium:
            return self._price + 0.5
        elif self.size == enums.ESize.Large:
            return self._price + 0.5 + 0.5
        else: 
            return self._price

    @property
    def recipe(self): 
        return self._recipe

class TheBoost(Juice):
    _RECIPE = {
        ingredient.Ingredient(enums.EIngredient.Mango): 0.5,
        ingredient.Ingredient(enums.EIngredient.Orange): 2,
        ingredient.Ingredient(enums.EIngredient.Guajana): 1
    }

    def __init__(self, size = enums.ESize.Small, price = 5):
        super().__init__("TheBoost", size, price, self._RECIPE)

class TheFresh(Juice):
    _RECIPE = {
        ingredient.Ingredient(enums.EIngredient.Apple): 3,
        ingredient.Ingredient(enums.EIngredient.Ginger): 1,
        ingredient.Ingredient(enums.EIngredient.Lemon): 1
    }
    
    def __init__(self, size = enums.ESize.Small, price = 4):
        super().__init__("TheFresh", size, price, self._RECIPE)

class TheFusion(Juice):
    _RECIPE = {
        ingredient.Ingredient(enums.EIngredient.Guava): 1,
        ingredient.Ingredient(enums.EIngredient.Pineapple): 0.25,
        ingredient.Ingredient(enums.EIngredient.Banana): 0.5
    }
    
    def __init__(self, size = enums.ESize.Small, price = 6):
        super().__init__("TheFusion", size, price, self._RECIPE)

class TheDetox(Juice):
    _RECIPE = {
        ingredient.Ingredient(enums.EIngredient.Carrot): 3,
        ingredient.Ingredient(enums.EIngredient.CeleryStick): 1,
        ingredient.Ingredient(enums.EIngredient.Beetroot): 1
    }
    
    def __init__(self, size = enums.ESize.Small, price = 3.5):
        super().__init__("TheDetox", size, price, self._RECIPE)