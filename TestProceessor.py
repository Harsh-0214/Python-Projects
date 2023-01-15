# Harsh Tamakuwala
#662282
# ICS4U0
# TestProcessor - testresultstp 
# Mr Veera
# march 19,2021
names=[]
answers=[]
infolist=[]

with open('testprocessortp.txt', 'r') as file:
    info=file.read()
    infolist=info.split("\n")
    print('All Information: ', infolist)
    
        
for index in range(0,len(infolist), 2):
    answers.append(infolist[index])

for num in range(1,len(infolist), 2):
    names.append(infolist[num])


print('Length of Information: ', len(infolist))
print('Info: ', infolist)
print('Names: ', names)
print('Answers: ', answers)
for 



