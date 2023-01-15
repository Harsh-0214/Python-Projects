##Harsh Tamakuwala
##662282
##Mr.Veera
##March 11, 2021
##Bowling using object oriented programming
from random import randint #used to create the throws

class bowler: #defines the class

    def __init__(self): #initializes every variable
        self.points=0 #sets points to 0
        self.pins=0 #sets number of pins knocked to zero
        self.throw=randint(0,10) #makes each throw a random number
        self.temp_points=0 #Needed for spares

    def setpoints(self): #Creates the scores, these are the 'throws'
        for turn in range(1,3): #2 throws per frame
            self.temp_points=0 #sets temporary points to 0 at the start of every turn
            self.throw=randint(0,11)#Throw has to be a random number
            self.pins=self.pins+self.throw#throw is also the number of pins that are knocked down
            if(self.pins<10 and turn==1): #If number of pins that are knocked down is less than a strike
                print('Turn:', turn, 'you hit ', self.pins, 'pins', 'you need', 10-self.pins, 'pins for a spare')
                self.temp_points+=self.pins
                self.throw=randint(0,self.pins)
                self.pins=self.pins+self.throw
                if(self.pins+self.temp_points>10 and turn==2): #If number of pins that are knocked down is less than a strike
                    self.points+=15 #adds 15 points because all pins were knocked down in two tries
                    self.throw=randint(0,11)
                    self.pins=0
                    return('Spare, +15 points!')
                else:
                    self.points+=self.temp_points
                    temp_points=0
                    
            elif(self.pins<10 and turn==2): #If 
                self.points+=self.temp_points+self.pins
                self.throw=randint(0,11)
                return('You hit', self.pins, 'more pins')
                
            elif(self.pins>=10 and turn==1): #if the number of pins is less than or equal to zero on the first turn then a strike has happened
                self.points+=20 #20 points are awarded
                self.throw=randint(0,11)
                self.pins=0
                return ('Strike, +20 points!')
        
    def getpoints(self):
        return('Total Points: ',self.points)
    def __repl__(self):
        return('Total Points: ',self.points)

player1=bowler()
number=1
for frame in range(1,11):
    print('FRAME', frame,': ')
    print('Frame', frame, ': ',player1.setpoints())
    print('Frame', frame, 'Score : ',player1.getpoints())
    
