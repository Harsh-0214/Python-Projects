# Ex 1 Section 13.2.4 Coder's Apprentice Adobe Pg 167.
# Mr Veera
# 01 April 2021

#My algorithm steps:
#1. Sort the given list
#2. Count the occurence of the fruit at index value 0 in the list
#3. Use the fruit at index value 0 of the sorted list as key
#   and its count as value to build the dictionary.
#4. Modify the list by removing all occurences of the fruit at index 0 of the list
#   to get a new list.
#5. Repeat steps 2,3 and 4 above until, there are no elements left in the list.

basket={} # empty dictionary
wordlist = ["apple","durian","banana","durian","apple","cherry","cherry","mango","apple","apple","cherry","durian","banana","apple","apple","apple","apple","banana","apple"]

# creating a copy of the given list 
new_list=[]
for item in wordlist:
    new_list.append(item)

wordlist.sort() # sorted the list in ascending order


##for fruit in new_list:
##    print(fruit, end=" ")
##    fruit_count=new_list.count(fruit)
##    basket[fruit]=fruit_count
##    print(fruit_count)
##    print(basket)
##    while(fruit_count>0):
##        new_list.remove(fruit)
##        fruit_count-=1
##    print(new_list)


# Using a nested loop to build the dictionary and modify the list as the fruits get
# added to the dictionary. 

while(True):
    if(len(wordlist)==0): # when this happens all the fuits in the list have been counted into the dictionary
        break
    fruit=wordlist[0]
    fruit_count=wordlist.count(fruit) 
    basket[fruit]=fruit_count # building the dictionary
# Modifying the list in this loop  by removing all the fruits in the list which are
# the same as at index 0.
    while(fruit_count>0):  
        wordlist.remove(fruit)
        fruit_count-=1
print(basket)
print(new_list)
