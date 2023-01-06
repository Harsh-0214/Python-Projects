##Harsh Tamakuwala
##662282
##Mr.Veera
##March 11, 2021
##Bowling using object oriented programming

from random import randint

class bowler:

    def __init__(self): #initializes each attribute
        self.turn=2 #each bowler gets two turns which are subtracted
        self.frame=10 #each bowler has 10 frames
        self.points=0 #initializes their points
        self.pins=10 #each bowler has 10 pins to hit
        self.word='' #'Strike' or 'Spare'
        self.throw=randint(0,10) #the bowlers turn/throw is a random number

    def taketurn(self):
            self.frame=self.frame-1 #decreases the frame number
            self.pins=(self.pins-self.throw) #random number is subtracted from self.pins which is 10, this finds out how many points should be rewarded
            self.turn=self.turn-1 #decreases the turn number

    def setpoints(self):
            if (self.pins<=0 and self.turn==1): #if the number of pins is less than or equal to zero on the first turn then a strike has happened
                self.points+=20 #20 points are awarded
                self.turn=2
                self.throw=randint(0,10)
                return ('Strike')
            elif(self.pins<=0 and self.turn==0): #proves that two turns were taken to clear the aisle therefore it is a spare
                self.points+=15 #15 points are awarded a spare
                self.turn=2
                self.throw=randint(0,10)
            elif(self.pins>0 and self.turn==0):
                self.points+=self.throw
                self.turn=0
                self.throw=randint(0,10)
                
    def getpoints(self):
        return ('Total Points: ', self.points, self.throw)
       
    def __repl__(self):
        return ('Score: {%2f}'.format(self.points))
        

player1=bowler()
while player1.frame>0:
    go=str(input('Press enter to take your turn'))
    if (go==''):
        player1.taketurn()
        print(player1.setpoints()) 
        print(player1.getpoints())
        #print(player1)


    
    
    
            
