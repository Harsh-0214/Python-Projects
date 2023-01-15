#Harsh Tamakuwala
#662282
#File Read Assignment
#ICS4U0
#Mr Veera
#March 19, 2021

info=[]
newinfo=[]
n=0
names=[]
scores=[]
r=[]
s=[]
d=[]

with open('input.txt','r') as file: ##Opens the file
    for line in file:
        info.append(line.rstrip('\n'))#Removes '\n'
    n=int(info[0]) #Changes n into an integer and adds it to the variable
    info=str(info) #changes the info list into a string so it can be re split
    newinfo=info.split(' ')## gets rid of the spaces between
    newinfo.pop(0)##Removes the n value from the list
    
print("All given Information: ", newinfo)
print('n value:' ,n)

for num in range(0,len(newinfo),4): ##Adds the names to the name list
    names.append(newinfo[num])

for num in range(1,len(newinfo),4): #puts the r values together
    r.append(int(newinfo[num]))
    
for num in range(2,len(newinfo),4):#puts the s values together
    s.append(int(newinfo[num]))

for num in range(3,len(newinfo),4):#puts the d values together
    d.append(newinfo[num])#--> can not be converted into an integer because of apostrophe' beside it
##for index in range(0,len(d)):
##    d[index].rstrip("'")
##print(d) #trying to fix it, did not work
    
for num in range(0, n):
    score=(2*r[num])+(3*s[num])#+d[num]) #--> d does not work as its values have an unremoveable ' attached to it so it cannot be converted into an integer
    scores.append(score)

winner1=names[scores.index(max(scores))] #Finds highest score in list
scores.pop(scores.index(max(scores))) #removes highest score from list
winner2=names[scores.index(max(scores))]# finds second highest score


print('R Values: ',r)
print('S Values: ',s)
print('D Values: ',d)
print('Computers: ', names)
print('Scores: ', scores)
print('The winners are :', winner1, winner2)
