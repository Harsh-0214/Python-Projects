#pg.270 PennyPitch
from random import randint
row1=[]
row2=[]
row3=[]
row4=[]
row5=[]
prize=''
whichprize=0
row=0
    
##ROW 1
while row <5:
    whichprize = randint(0,5)
    if whichprize == 0:
        prize ='    '
        row1.append(prize)
        row+=1
    elif whichprize == 1:
        prize ='PUZZLE'
        row+=1
        row1.append(prize)
    elif whichprize == 2:
        prize ='BALL'
        row+=1
        row1.append(prize)
    elif whichprize == 3:
        prize ='POSTER'
        row1.append(prize)
        row+=1
    elif whichprize == 4:
        prize ='DOLL'
        row1.append(prize)
        row+=1
    elif whichprize == 5:
        prize ='GAME'
        row1.append(prize)
        row+=1
row=0
##ROW2
while row <5:
    whichprize=randint(0,5)
    if whichprize == 0:
        prize ='    '
        row2.append(prize)
        row+=1
    elif whichprize == 1:
        prize ='PUZZLE'
        row2.append(prize)
        row+=1
    elif whichprize == 2:
        prize ='BALL'
        row2.append(prize)
        row+=1
    elif whichprize == 3:
        prize ='POSTER'
        row2.append(prize)
        row+=1
    elif whichprize == 4:
        prize ='DOLL'
        row2.append(prize)
        row+=1
    elif whichprize == 5:
        prize ='GAME'
        row2.append(prize)
        row+=1
row=0
##ROW3
while row <5:
    whichprize=randint(0,5)
    if whichprize == 0:
        prize ='    '
        row+=1
        row3.append(prize)
    elif whichprize == 1:
        prize ='PUZZLE'
        row3.append(prize)
        row+=1
    elif whichprize == 2:
        prize ='BALL'
        row3.append(prize)
        row+=1
    elif whichprize == 3:
        prize ='POSTER'
        row3.append(prize)
        row+=1
    elif whichprize == 4:
        prize ='DOLL'
        row3.append(prize)
        row+=1
    elif whichprize == 5:
        prize ='GAME'
        row3.append(prize)
        row+=1
row=0
##ROW4
while row <5:
    whichprize=randint(0,5)
    if whichprize == 0:
        prize ='    '
        row4.append(prize)
        row+=1
    elif whichprize == 1:
        prize ='PUZZLE'
        row4.append(prize)
        row+=1
    elif whichprize == 2:
        prize ='BALL'
        row4.append(prize)
        row+=1
    elif whichprize == 3:
        prize ='POSTER'
        row4.append(prize)
        row+=1
    elif whichprize == 4:
        prize ='DOLL'
        row4.append(prize)
        row+=1
    elif whichprize == 5:
        prize ='GAME'
        row4.append(prize)
        row+=1
row=0
##ROW5
while row <5:
    whichprize=randint(0,5)
    if whichprize == 0:
        prize ='    '
        row5.append(prize)
        row+=1
    elif whichprize == 1:
        prize ='PUZZLE'
        row5.append(prize)
        row+=1
    elif whichprize == 2:
        prize ='BALL'
        row5.append(prize)
        row+=1
    elif whichprize == 3:
        prize ='POSTER'
        row5.append(prize)
        row+=1
    elif whichprize == 4:
        prize ='DOLL'
        row5.append(prize)
        row+=1
    elif whichprize == 5:
        prize ='GAME'
        row5.append(prize)
        row+=1
row=0

print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
