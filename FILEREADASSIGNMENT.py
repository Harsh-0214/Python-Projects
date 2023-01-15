#Harsh Tamakuwala
#662282
#File Read Assignment
#ICS4U0
#Mr Veera
#March 19, 2021
R=0
S=0
D=0
name=[]
n=0
string=''

with open('input.txt','r') as file:
    info=file.read()
    n=info[0]
    split_n_info=info.split('\n')
    split_n_info.pop(0)
    print('Split n Info: ',split_n_info)
    print('n:', n)

print('info', split_n_info)

for num in range(0,len(split_n_info)):
    string+=split_n_info[num]

string.split(" ")
print('string', string)
    

                 


##for index in range(0,)
#score=(2*R)+(3*S)+D
#.append(score)







