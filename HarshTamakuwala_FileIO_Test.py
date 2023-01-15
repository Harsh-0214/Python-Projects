#Harsh Tamakuwala
#662282
#Mr.Veera
#File-I/O-Big Bang
#March 30, 2021

contents=[]

file=open('Xs.txt','r')

for line in file:
    contents.append(line.rstrip('\n')) #removes '\n'

k=int(contents[0])

if k>10: #if k is more than 10 user will be prompted to enter another shift value in its place
    print('Please enter a Number below 10')
    k=int(input('Enter a Shift Value:'))

encoded=str(contents[1]) #gets encoded message
encoded=encoded.upper()## makes all characters uppercase

#Alphabet List
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",'R','S','T','U','V','W','X','Y','Z']

#Initializing Variables
decoded = []
position=0
#Changes the characters at each position depending on the shift value(k) and then changes the position until end of string
#Also has an if condition which checks if the letter passes the end of the alphabet and if true, it sends the value to 1 which is "A"
for i in encoded:
    position +=1
    s=(3*position+k)
    if s < -26:
        s += 26
    decoded.append(alphabet[alphabet.index(i) - s])
    final=''.join(decoded)

print(final)


file.close()

file=open('Decoded.txt','w')

file.write(final)

file.close()
