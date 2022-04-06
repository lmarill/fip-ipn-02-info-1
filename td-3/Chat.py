from enum import Enum


class Classification(Enum):
    POISSON     = 0
    INSECTE     = 1
    OISEAU      = 2
    MAMIFERE    = 3
    AMPHIBIEN   = 4
    REPTILE     = 5
    IVERTEBRER  = 6


class Animal:
    _nom = ""
    _classification = None

    def __init__(self, nom, classification):
        self._nom = nom
        self._classification = classification
        print("L'animal : " + self._nom + " à été crée |type : " + str(self._classification))

    @property
    def classification(self):
        return self._classification


class Chat(Animal):

    def __init__(self, nom, classification):
        super().__init__(nom, classification)
        print("Le chat : " + self._nom + " à été crée |type : " + str(self._classification))

class Chien(Animal):

    def __init__(self, nom, classification):
        super().__init__(nom, classification)
        print("Le chien : " + self._nom + " à été crée |type : " + str(self._classification))


chat = Animal("Osama", Classification.MAMIFERE)
chat = Chat("Minou", Classification.MAMIFERE)
chat = Chien("Rheun", Classification.MAMIFERE)
