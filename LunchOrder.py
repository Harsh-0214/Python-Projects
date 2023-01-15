#Harsh Tamakuwala
#662282
#Mr. Veera
#Ex. 3 Pg. 209 - LunchOrder
#March 1st, 2021

class lunchorder:

    def __init__(self):
        self.order=0

    def hamburgers(self, hamburgers):
        order=order+(hamburgers*1.85)
        return ('Each hamburger has 9.0g of fat, 33.0g of carbs, and 1.0g of fiber. ')

    def salads(self, salads):
        order=order+(salads*2.00)
        return ('Each salad has 1.0g of fat, 11.0g of carbs, and 1.0g of fiber. ')
    
    def fries(self, fries):
        order=order+(fries*1.30)
        return ('French Fries has 9.0g of fat, 33.0g of carbs, and 1.0g of fiber. ')
    
    def sodas(self, sodas):
        order=order+(sodas*0.95)
        return ('Each soda has 9.0g of fat, 33.0g of carbs, and 1.0g of fiber. ')

    def __repl__(self):
        return ('Your Order comes to: ', order)

food=lunchorder()


food.hamburgers(int(input('Enter number of hamburgers: ')))
food.salads(int(input('Enter number of salads: ')))
food.fries(int(input('Enter number of fries: ')))
food.sodas(int(input('Enter number of sodas: ')))

print(food)

