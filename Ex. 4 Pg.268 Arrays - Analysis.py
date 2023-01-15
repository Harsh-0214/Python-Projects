#Harsh Tamakuwala
#662282
#Mr.Veera
#Ex. 4 Pg.268 Arrays - Analysis

#Variables and Lists
i=0
index=0
total=0
average=0
numbers=[]
first=''
second=''
third=''
fourth=''
fifth=''
sixth=''
seventh=''
eighth=''
ninth=''
tenth=''
s='*'
#input
while (i==0):
    user=int(input('Enter a number from 0-50, to finish, enter a number above 50: '))
    if (user>50):
        break
    elif (user<0):
        break
    elif (user==1 or user==2 or user==3 or user==4 or user==5):
        first+=s
        numbers.append(user)
    elif (user==6 or user==7 or user==8 or user==9 or user==10):
        second+=s
        numbers.append(user)
    elif (user==11 or user==12 or user==13 or user==14 or user==15):
        third+=s
        numbers.append(user)
    elif (user==16 or user==17 or user==18 or user==19 or user==20):
        fourth+=s
        numbers.append(user)
    elif (user==21 or user==22 or user==23 or user==24 or user==25):
        fifth+=s
        numbers.append(user)
    elif (user==26 or user==27 or user==28 or user==29 or user==30):
        sixth+=s
        numbers.append(user)
    elif (user==31 or user==32 or user==33 or user==34 or user==35):
        seventh+=s
        numbers.append(user)
    elif (user==36 or user==37 or user==38 or user==39 or user==40):
        eighth+=s
        numbers.append(user)
    elif (user==41 or user==42 or user==43 or user==44 or user==45):
        ninth+=s
        numbers.append(user)
    elif (user==46 or user==47 or user==48 or user==49 or user==50):
        tenth+=s
        numbers.append(user)
#average
average=sum(numbers)//len(numbers)

min_val = min(numbers)
max_val = max(numbers)
rge=max_val-min_val

print('List:',numbers)
print('Average: ', average)
print('maximum: ',max_val)
print('range:',rge)

print('1-5: ',first)
print('6-10: ',second)
print('11-15: ',third)
print('16-20: ',fourth)
print('21-25: ',fifth)
print('26-30: ',sixth)
print('31-35: ',seventh)
print('36-40: ',eighth)
print('41-45:',ninth)
print('46-50:',tenth)



    
        
