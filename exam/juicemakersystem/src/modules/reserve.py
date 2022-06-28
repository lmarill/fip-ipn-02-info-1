from cmath import log


class Reserve():
    _ingredients = None
    _recipes = None

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        self._ingredients = ingredients

    @property
    def recipes(self):
        return self._recipes

    @recipes.setter
    def recipes(self, recipes):
        self._recipes = recipes

    def getAvailibility(self):
        if self._recipes is None:
            raise BaseException('cannot check availibility, no recipes specify!')
        
        if self._recipes is None:
            raise BaseException('cannot check availibility, no ingredients specify!')

        juices = {}
        for juice in self._recipes:
            # filtered the reserve
            filtered = {}
            for ingInRec in [k for k in juice.recipe.keys()]:
                for ingInRes, qte in self._ingredients.items():
                    if (ingInRes.name == ingInRec.name):
                        filtered[ingInRes] = qte
            
            # calculated amount of available juice
            nbAvailable = []
            for ingInRes, qteRes in filtered.items():
                for ingInRec, qteRec in juice.recipe.items():
                    if ingInRec.name == ingInRec.name:
                        temp = int(qteRes / qteRec)
                        if temp not in nbAvailable:
                            nbAvailable.append(temp)

            juices[juice] = min(nbAvailable)

        return juices

    def takeIngredients(self, juices):
        if self._ingredients is None:
            raise BaseException("cannot take from reserve, no ingredients loaded")

        for juice, nbJuice in juices.items():
            for ingInRec in [k for k in juice.recipe.keys()]:
                for ingInRes, qteInRes in self._ingredients.items():
                    if (ingInRes.name == ingInRec.name):
                        remains = qteInRes - nbJuice * juice.recipe[ingInRec]
                        if remains >= 0:
                            self._ingredients[ingInRes] = remains
                        else:
                            raise BaseException("Cannot take from reserve, not enough %s for %s preparation" % (ingInRes.name, juice.name))
