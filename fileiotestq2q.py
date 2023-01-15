#Harsh Tamakuwala
#662282
#Mr.Veera
#File-I/O Test-straight road - Q2
#March 30, 2021

file=open('input.txt', 'r') #retrieving contents from file containing the 4 integers
for line in file:
    contents=line.split(' ') #creates a list with those integers

print ('contents: ',contents) #prints contents

file.close()

intcontents = []

for i in range(len(contents)):
  intcontents.append(int(contents[i])) #converts list of strings to list of integers

print('n',intcontents)

length = 5 #length of every input will be 5 integers because of the five cities

for i in range(5): #i represents initial city locations
  final = ""  
  
  for car in range(5): #j represents the car as it moves through each city
    if car == i: #if the car and the city location is equal then the distance would be 0
      final += str(0) #adds a distance of 0 to the final answer 
      
    elif car > i: #if car position is greater than city position
      addnum = 0
      for x in intcontents[i:car]: #adds the next distance which is stated in the input
        addnum += x
      final += (str(addnum))#adds to the final answer
    
    elif car < i: #if car position is less than city position
      addnum = 0
      for x in intcontents[car:i]:
          addnum += x
      final += (str(addnum))
    
    if car < length:
      final += " "
  
  print(final)

  file=open('output.txt', 'a') #outputs into output file

  file.write(final)
  file.write('---')

  file.close()
