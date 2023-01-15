#Harsh Tamakuwala
#662282
#CCC 2011 J4: Boring Business

#Designing each row and declaring them as lists
row1=['','','','#','','','','','','','','','','']
row2=['','','','#','','','','','','','','','','']
row3=['','','','#','#','#','#','','#','#','#','','','']
row4=['','','','','','','#','','#','','#','','','']
row5=['','','#','','','','#','#','#','','#','','','']
row6=['','','#','','','','','','','','#','','','']
row7=['','','#','#','#','#','#','#','#','#','#','','','']
row8=['','','','','','','','','','','','','','']
#adding lists into 'excavation' which makes the 2d list
excavation=[row1, row2, row3, row4, row5, row6, row7, row8]
#arranging the list
for symbols in range(len(excavation)):
    for rows in range(len(row1)):
        print(excavation[symbols][rows]," ",end="")
    print()
#making/clearing variables
d=0
l=0
r=0
u=0
q=0
danger=(False)
#these coordinates should be 3 and 5 but since the list counts zero first they both decreased by one
vertical=4
horizontal=2
#Down Value
d=int(input('enter the DOWN value, zero does not change the position: '))

if (d!=0): #recognizes that the spot is taken
    if (d>=8):#restrictions depending on the size of the list and how many spots it can go without causing being dangerous
        danger=(True)#if it passes 8 it prints danger and puts an X on the dangerous area
        excavation[vertical][horizontal]='X'
        print(vertical,'', horizontal, 'DANGER')
    elif(d>0):
        vertical+=d
        if (excavation[vertical][horizontal]!=''):
            danger=(True)
            excavation[vertical][horizontal]='X'
            print('DANGER')
        else:
            excavation[vertical][horizontal]='+' 


l=int(input('enter the LEFT value, zero does not change the position: '))
if (l!=0):
    if (l>=3):
        danger=(True)
        excavation[vertical][horizontal]='X'
        print('DANGER')
    elif(l>0):
        horizontal-=l
        if (excavation[vertical][horizontal]!=''):
            danger=(True)
            excavation[vertical][horizontal]='X'
            print('DANGER')
        else:
            excavation[vertical][horizontal]='+'
r=int(input('enter RIGHT value, zero does not change the position: '))
if (r!=0):
    if (r>9):
        danger=(True)
        excavation[vertical][horizontal]='X'
        print('DANGER')
    elif(r>0):
        horizontal+=r
        if (excavation[vertical][horizontal]!=''):
            danger=(True)
            excavation[vertical][horizontal]='X'
            print('DANGER')
        else:
            excavation[vertical][horizontal]='+'
u=int(input('enter UP value, zero does not change the position: '))
if (u!=0):
    if (u>8):
        danger=(True)
        excavation[vertical][horizontal]='X'
        print('DANGER')
    elif(u>0):
        vertical-=u-1
        if (excavation[vertical][horizontal]!=''):
            danger=(True)
            excavation[vertical][horizontal]='X'
            print('DANGER')
        else:
            excavation[vertical][horizontal]='+'
            
q=int(input('enter a value to quit, zero keeps it running: '))
if (q==0):
    for symbols in range(len(excavation)):
        for rows in range(len(row1)):
            print(excavation[symbols][rows]," ",end="")
        print()
        

