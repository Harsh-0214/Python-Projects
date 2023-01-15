# Lesson on Reading from a file
# ICS4U0
# Mr Veera
# 07 May 2018

# Code opens a data file, reads its contents and prints it on the screen
# Code uses read() function
# Every Open() function should have a corresponding close() function
# The following code reads the whole file into a single string 'contents'.
file = open('data.txt', 'r')
contents = file.read()
print(contents)
file.close()
print("-")
## Code uses 'with' operator
## The with operator automatically introduces a file 'close()' function.
with open('data.txt', 'r') as file:
    for line in file:
        print(line)
        print(len(line))

print("-")
####
##
####code converts the contents of a file as a list of strings
####using the list() function
file = open('data.txt', 'r')
contents=list(file)
print(contents)
file.close()


print("-")
###### Code does the same operation as above, but uses the readlines() function.
file = open('data.txt', 'r')
contents_again=file.readlines()
print(contents_again)
file.close()
####
print("-")

file = open('data.txt', 'r')
for line in file:
    print(line)
file.close()
