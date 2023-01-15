#Harsh Tamakuwala
#662282
#Mr.Veera
#April 20, 2021
#Final Evaluation Question 1

import sys # used for try and except messages, if error occurs the program will be stopped

#Defining Variables

count=1 ## used for adding the different lines of the file

chars='\n' #used to strip new line character in line 'a'

good=True #used when deciding whether pairing is done right or not, changed to false if not done right
try: #checks if file is there
    with open('Input.txt', 'r') as file: ##opens file
        for line in file: #checks each line
        
            if (count==1): #since there will always be 3 lines, we can easily seperate them into their own individual variables based on the numbered line they are in
                try: #trys converting line into an integer
                    n=int(line) #sends first line to n and convert to an integer
                except: #if the line does not contain an integer
                    print("****Error: Please enter a number in the first line****") #error message
                    sys.exit() #ends program because of error
                count+=1 # moves to second line
                
            elif(count==2):
                    a=line.split(' ') # first set of names
                    a[(n-1)]=a[(n-1)].rstrip(chars) # strips the newline character
                    count+=1
                       
            elif(count==3):
                b=line.split(' ') #second set of ordered names
except: #if file isnt found, program is ended
    print('file not found')
    sys.exit('program ended.')

print('n: ',n)
print('set 1: ',a)
print('set 2: ',b)

dictionary={'set1':a, 'set2': b} #adds each set to the dictionary


good=True

for i in range(n): #compares names in both sets 'n' times
    dictionary['set1']=a[i] 
    dictionary['set2']=b[i]
    if dictionary['set1']==dictionary['set2']: #checks if partners names are different
        good=False #if they are the same then it means that they are paired with themselves which is not good therefore, good=false

if good==True: #if good == True then all compared names were different so everyone has their own partner
    print('Good')
else:
    print('Bad')
