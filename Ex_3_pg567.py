import random
numbers=[]
for i in range(500):
    temp=random.randint(0,9)
    numbers.append(temp)

print('Number:      Occurances:')
for i in range (10):
    print(i,'           ',numbers.count(i))
