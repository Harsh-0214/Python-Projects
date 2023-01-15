# Review Stats Adobe Pg 707 ( Textbook Pg 317)
# Mr Veera
# 17 Mar 2021
# ICS4U0

test_details=[]
names=[]
grades=[]
with open("test1.dat", "r") as file:
    for line in file:
        test_details.append(line.rstrip("\n"))
#    test_details=file.readlines()
#    test_details=list(file)

#print(test_details)
#file.close()

##for name in range(0,len(test_details),2):
##    names.append(test_details[name])
##print(names)
##
##for marks in range(1,len(test_details),2):
##    grades.append(int(test_details[marks]))
##print(grades)

for item in test_details:
    if(item.isdigit()):
        grades.append(int(item))
    else:
        names.append(item)
        
print(names)
print(grades)


