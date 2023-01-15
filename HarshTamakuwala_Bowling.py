##Harsh Tamakuwala
##662282
##Mr.Veera, ICS4U0
##Exercise 7, pg 211, Bowling
##March 12, 2021

import random #used to generate random number for the throws

class bowling: #defining the class
    def __init__(self): # initializing all variables
        self.totalpoints=0 #points for each player
        self.throw=random.randint(0,10)#throw must be a random number
        self.leftovers=0 # how many pins are left after the first throw
        self.players=0 #number of players
        self.second_throw=0 #second throw
        self.frame=0 #frame number
        self.totalpins=0 #number of total pins hit is intiially 0
        
    def playgame(self): #function that starts the game and plays it through
        pointslist=[] #list that contains the final scores
        print('Welcome to Bowling!')
        players=int(input('How many players are there: ')) #prompt asking for number of players
        for player in range(1, (players)+1): #loop depending on how many players there are
            totalpoints=0 #initializing points again for each player
            for frame in range(1,11): #10 frames
              throw=random.randint(0,10) #throw can be a number from 0 to 10

              if (throw == 10): #checks if a strike has happened (all 10 pins being hit)
                  print('Player ',(player), 'STRIKE! +20 Points') #if true, 20 points are awarded
                  totalpoints+=20
                  print('Total Points =', totalpoints) #prints total points for the player
                  print() #makes a space
                  print('Frame', frame) #prints frame number
                  frame+=1 #moves to the next frame
              else: #if not all 10 pins are hit then it checks for spares or adds points per pins
                print() #makes a space
                print('Turn 1: ', 'Player', player, 'hit', throw, 'pins')#prints
                leftovers=10-throw #determines how many pins are left standing after the first throw
                second_throw= random.randint(0,leftovers)
                if (second_throw==leftovers): #if the second throw hits all the left over pins, it is considered a spare so 15 points are awarded
                    totalpoints+=15 #15 points are awarded
                    print('Player', (player), 'You hit', leftovers, 'pins, SPARE! +15 Points') #prints how many pins were hit and how many points were awarded
                    print('Total Points = ', totalpoints) #prints total points
                    print() #prints a space
                    print('Frame', frame) #prints the frame number
                    frame+=1 #moves to next frame
                elif (second_throw!= leftovers): #if not all the leftover pins are hit
                    totalpins=throw+second_throw #pins hit is equal to both throws 
                    print('Turn 2: Player', player, 'Knocked down ', totalpins) #prints how many pins were hit in the two rounds
                    totalpoints+=totalpins #adds a point per pin
                    print('Total Points = ', totalpoints) #prints total points for the player
                    print() #prints a space
                    print('Frame', frame) #prints the frame
                    frame+=1 #moves to the next frame
            print('Player', player, 'final score is: ', totalpoints) #Prints the players final score
            pointslist.append(totalpoints) #adds the final scores to the list

        winner=max(pointslist) #finds the highest score in the list to determine the winner
        print() #prints a space
        print ('Winner: Player', (pointslist.index(winner))+1) #prints the winner
        
    def __repl__(self): #when object is printed
        return ('WINNER -------->> PLAYER '((pointslist.index(winner))+1), 'CONGRATULATIONS!!!')

#Client Code
game=bowling() #intitializes all variables
game.playgame() #starts the playgame function
print(game) #activates repl function

    

                      
                  
              
              
              
