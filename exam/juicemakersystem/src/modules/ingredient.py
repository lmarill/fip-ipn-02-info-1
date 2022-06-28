from argparse import ArgumentTypeError
import modules.enums as enums

class Ingredient():
    _type: None

    def __init__(self, type): 
        if not isinstance(type, enums.EIngredient):
            raise ArgumentTypeError("type must be a EIngredient")
        self._type = type

    @property
    def name(self):
        return self._type.name