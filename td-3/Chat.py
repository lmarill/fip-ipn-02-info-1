from enum import Enum
from argparse import ArgumentTypeError


class Classification(Enum):
    POISSON = 0
    INSECTE = 1
    OISEAU = 2
    MAMIFERE = 3
    AMPHIBIEN = 4
    REPTILE = 5
    IVERTEBRER = 6


class Animal:
    _nom = ""
    _classification = None
    _isCute = False
    _age = 0

    def __init__(self, nom, classification, age=0, cutness=False):
        if not isinstance(nom, str):
            raise ArgumentTypeError("must be string")
        if not isinstance(classification, Classification):
            raise ArgumentTypeError("must be Classification")
        if not isinstance(cutness, bool):
            raise ArgumentTypeError("must be boolean")
        if not isinstance(age, int):
            raise ArgumentTypeError("must be int")

        self._nom = nom
        self._classification = classification
        self._isCute = cutness
        self._age = age
        # print("L'animal : " + self._nom + " à été crée |type : " + str(self._classification))

    @property
    def classification(self):
        return self._classification

    @property
    def isCute(self):
        return self._isCute

    @property
    def nom(self):
        return self._nom

    @property
    def age(self):
        return self._age


class Chat(Animal):
    def __init__(self, nom, classification=Classification.MAMIFERE, age=0):
        super().__init__(nom, classification, age, True)
        # print("Le chat : " + self._nom + " à été crée |type : " + str(self._classification))


class Chien(Animal):
    def __init__(self, nom, classification=Classification.MAMIFERE, age=0):
        super().__init__(nom, classification, age)
        # print("Le chien : " + self._nom + " à été crée |type : " + str(self._classification))

chat = Chat("Minou")
chien = Chien("Rheun")
