import modules.enums as enums
import modules.juice as juice
from modules.ingredient import Ingredient
from modules.reserve import Reserve
from modules.barmaid import Barmaid

if __name__ == "__main__":
    stocks = {
        Ingredient(enums.EIngredient.Apple): 100,
        Ingredient(enums.EIngredient.Banana): 100,
        Ingredient(enums.EIngredient.Beetroot): 100,
        Ingredient(enums.EIngredient.Carrot): 100,
        Ingredient(enums.EIngredient.Ginger): 100,
        Ingredient(enums.EIngredient.CeleryStick): 100,
        Ingredient(enums.EIngredient.Guajana): 100,
        Ingredient(enums.EIngredient.Lemon): 100,
        Ingredient(enums.EIngredient.Mango): 100,
        Ingredient(enums.EIngredient.Guava): 100,
        Ingredient(enums.EIngredient.Orange): 100,
        Ingredient(enums.EIngredient.Pineapple): 100
    }

    recipes = [
        juice.TheBoost(),
        juice.TheFresh(),
        juice.TheDetox(),
        juice.TheFusion()
    ]

    order = {
        juice.TheBoost(size=enums.ESize.Large): 1,
        juice.TheFresh(size=enums.ESize.Small): 2,
        juice.TheDetox(size=enums.ESize.Medium): 1,   
    }

    reserve = Reserve()
    bill = Barmaid("Bill")
    
    # Bill prepare the day
    bill.prepareReserve(stocks, reserve)
    bill.prepareRecipes(recipes, reserve)
    ingredients = bill.checkReserve(reserve)
    print("ingredients availability:\n- %s" % ("\n- ".join("%s: qte=%d" %(ing.name, qte) for ing, qte in ingredients.items())))
    available = bill.checkAvailability(reserve)
    print("juice availability:\n- %s" % ("\n- ".join("%s: qte=%d" %(juice.name, qte) for juice, qte in available.items())))

    # Bill check for an order, can we prepare this order?
    bill.checkOrder(order, reserve)
    print("you ordered for:\n -%s" % ("\n- ".join("%d %s for $%d" %(qte, juice.name, qte * juice.price) for juice, qte in order.items())))

    # Bill give the bill of the order, validate the command and take the money
    totalPrice = bill.giveTheBillForOrder()
    print("total price of the order: $%d" % totalPrice)
    bill.validateOrder()
    (payed, remains) = bill.getMoneyForOrder(totalPrice)
    print("payed? %s (remains=%d)" % (payed, remains))

    # Bill prepare the order
    juices = bill.prepareOrder(reserve)
    #print("you got your command :)\n -%s" % ("\n- ".join(  )))

    # Bill checks the reserve
    ingredients = bill.checkReserve(reserve)
    print("ingredients availability:\n- %s" % ("\n- ".join("%s: qte=%d" %(ing.name, qte) for ing, qte in ingredients.items())))
    available = bill.checkAvailability(reserve)
    print("juice availibity:\n- %s" % ("\n- ".join("%s: qte=%d" %(juice.name, qte) for juice, qte in available.items())))


