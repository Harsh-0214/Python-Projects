#Page 182, Review: Coin - part 1 of 2

from random import randint

class Coin:
    def __init__(self, face):
        self.faceUp = face
        
    def flipCoin(self):
        self.faceUp = randint(0,1)
        
    def showFace(self):
        return self.faceUp
    
    def __repr__(self):
        if self.faceUp == 0:
            return ("The coin's face is heads")
        else:
            return ("The coin's face is tails")

nickel = Coin(1)

print("The current face is {}".format(nickel))

nickel.flipCoin()

print("The new face is {}".format(nickel))
