#Harsh Tamakuwala
#662282
#Mr.Veera
#Feb 13,2021
#CCC 2014 J4 Party Invitation


k = int(input('How many friends? '))

#Create friends list[1.2..k]
friends = []
for i in range (k):
    friends.append(i+1)

m = int(input('How many rounds? '))

for round in range(m):
    r = int(input('Value of r: '))

    #Eliminate every rth friend
    newfriends = []
    for i in range(len(friends)):
        if (i+1) % r != 0: #if the remainder of (i+1)/r does not equal 0 then...
            newfriends.append (friends[i])

    #Copy the new friends list back into the old friends list
    friends = []
    for f in newfriends:
        friends.append(f)

for f in friends:
    print (f)
