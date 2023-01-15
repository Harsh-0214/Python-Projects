#Harsh Tamakuwala
#662282
#ICS4U0
#Mr Veera
#Simple Statistics - only works with single positive digits. example(-1 and 36 would not work and they would cause errors because of the multiple index values being taken up)
#26 Mar 2021

import statistics #used to find median

#CREATES THE FILE

filename=str(input('Enter name of the file: ')) #prompt to get the name and create a file

file=open(filename,'w') #write function

while True:
    text = input("Please enter a line of text( double 'Enter' keystroke to end): ")
    if text=='':
        break
    else:
        text=text+'\n'
        file.write(text)
        
file.close()

#INITIALIZING VARIABLES

contents=[] #intitial list with line info
intcontents=[] #when info is converted to integers
ordered=[] #final statement list
n=0 # n value
minimum=0 # minimum value
quart1=[] #first quartile
mquart1=0 #first quartile median
median=0 #median of whole line
quart3=[] #third quartile
mquart3=0 #third quartile median
maximum=0 # maximum value of entire line
skew='' #type of skew...ex.'right-skewed', 'symmetric', 'left-skewed'
filename2='analyzed_data'

#clears analyzed data file
file=open(filename2, 'w')
file.write(' ')
file.close()

#READING THE FILE INFO

file=open(filename,'r')

##creating intial lists, removing spaces, getting info ready to find desired variables
for line in file: ##prints line by line
    if (line[0]!='0'): #checks if n value is not 0 otherwise doesnt run for that line  
        for index in range(0, len(line), 2): #gets rid of spaces(' ') and ('\n') by using a 2-step loop
            contents.append(line[index]) #brings line into the content list
            
        for num in range(0, len(contents)):
            intcontents.append(int(contents[num]))#converts initial list into a list with integer values instead
            n=intcontents[0] #changes variable to n value of the line
        print('n: ',n)
        print('contents: ', contents)
        intcontents.pop(0) #removes n value
        intcontents.sort() #sorts from least to greatest
        print('intcontents: ',intcontents)
        
        #finds minimum value of sorted list
        minimum=min(intcontents)
        print('minimum: ',minimum)

        #finds median of sorted list
        median=statistics.median(intcontents)
        print('median: ',median)

        #finds maximum value in sorted list
        maximum=max(intcontents)
        print('maximum: ',maximum)

        #creates a list with the values of the first quartile and then finds its median
        for num in range(0,n//2):
            quart1.append(intcontents[num])
        mquart1=statistics.median(quart1)
        print('quart1: ',quart1, "1st quartile median:", mquart1)

        #creates a list with the values of the third quartile and then finds its median
        for num in range(n//2,n):
            quart3.append(intcontents[num])
        mquart3=statistics.median(quart3)
        print('quart3: ',quart3, "3rd quartile median:", mquart3)

        #finding the skewness
        if ((maximum-median>median-minimum) or (((maximum-median)==(median-minimum)) and ((mquart3-median)>(median-mquart1)))):
            skew='right-skewed'
        elif ((maximum-median<median-minimum) or (((maximum-median)==(median-minimum)) and ((mquart3-median)<(median-mquart1)))):
            skew='left-skewed'
        else:
            skew='symmetric'

        #adding all values to the final statement
        ordered.append(minimum)
        ordered.append(mquart1)
        ordered.append(median)
        ordered.append(mquart3)
        ordered.append(maximum)

        print("Final:",ordered, skew)
        intcontents.clear() ##clears for next line
        contents.clear()

        #adds to analyzed data file , appends this time because of possibility of multiple lines
        file=open(filename2, 'a')
        finalstatement=(str(ordered),skew)
        file.write(str(finalstatement))

        file.close()

        ordered.clear() #clears for next line
    
file.close()


