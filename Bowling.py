from random import randint

class bowling:
    def __init__(self):
        self.pins=0

    def throw(self):
        self.pins=random.randint(0,10)

    def __repl__(self)
        
class points:
    def __init__(self):
        self.points=0
    def strike(self):
        self.points=self.points+20
        return ('Strike')
    
    def setscore(self):
        pass

    def getscore(self):
        return self.points
        

throw1=bowling()
throw2=bowling()
throw1.throw()
throw2.throw()

for range in (0,10):
    input("Press enter to bowl")
    throw1.throw()
    if (throw1.pins==10):
        throw1.strike()
    else:
        break

print()
        
    
    
