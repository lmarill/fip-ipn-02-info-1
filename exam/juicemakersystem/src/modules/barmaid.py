class Barmaid():
    _name = ""
    _bill = 0
    _validated = False
    _payed = False
    _order = None

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def bill(self):
        self._bill = 0
        for juice, qte in self._order.items():
            self._bill += juice.price * qte
        return self._bill

    def prepareReserve(self, ingredients, reserve):
        reserve.ingredients = ingredients

    def prepareRecipes(self, recipes, reserve):
        reserve.recipes = recipes

    def checkReserve(self, reserve): 
        return reserve.ingredients
    
    def checkRecipes(self, reserve):
        return reserve.recipes

    def checkAvailability(self, reserve): 
        return reserve.getAvailibility()

    def checkOrder(self, order, reserve):
        # if order already exist
        if self._order != None: 
            raise BaseException("cannot check order, an order is already in progress!")

        # then check the reserve
        available = self.checkAvailability(reserve)
        for juice, qte in order.items():
            if juice.name not in [k.name for k in available.keys()]:
                raise BaseException('cannot check order, this juice is no more available: %s' % (juice.name))
            else:
                for k, v in available.items():
                    if juice.name == k.name:
                        if qte > v:
                            raise BaseException('cannot check order, you order more than we have! (juice=%s, order=%d, stock=%d)' % (juice.name, qte, v))
        
        # we can prepare this order
        self._order = order
        return True

    def cancelOrder(self):
        self._order = None
        self._payed = False
        self._validated = False

    def validateOrder(self):
        if self._order == None:
            raise BaseException("cannot validate order, no order in progess")

        self._validated = True
        return self._validated

    def giveTheBillForOrder(self): 
        if self._order == None:
            raise BaseException("cannot give the bill, no order in progress")
            
        return self.bill

    def getMoneyForOrder(self, sumOfMoney): 
        if self._order == None: 
            raise BaseException("cannot pay order, no order in progess")

        if not self._validated:
            raise BaseException("cannot pay order, the order is not validated")

        remains = sumOfMoney - self.bill
        if remains < 0:
            self._payed = False
        else:
            self._payed = True
        return (self._payed, remains)

    def prepareOrder(self, reserve):
        if self._order == None: 
            raise BaseException("cannot prepare order, no order in progess")

        if not self._validated:
            raise BaseException("cannot prepare order, the order is not validated")

        if not self._payed:
            raise BaseException("cannot prepare order, the order is not payed")

        reserve.takeIngredients(self._order)
        return self._order

    
    



