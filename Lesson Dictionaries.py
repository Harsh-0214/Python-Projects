# Lesson on Dictionaries
# ICS4U0
# Mr Veera
# 26 Nov 2019

# Reference book used " Coders Apprentice", Chapter 13.

# Dictionaries are an unordered collection of elements. Every element is associated with a key.
# Dictionaries store 'key:value" combinations. In the following dictionary,
# the strings are the keys while the integer values are the values.

fruitbasket = { "apple":3, "banana":5, "cherry":50 }

## values are accessed via the keys

print('key', fruitbasket["banana"])

# You can use a for loop to traverse a dictionary.
# The variable in the for loop gets access to
# all the keys.

fruitbasket = { "apple":3, "banana":5, "cherry":50 }
for key in fruitbasket:
    print( "{}:{}".format( key , fruitbasket[key] ))
##
### A new element can be added to a dictionary by assigning
### a value to the dictionary item identified by a new key.
### For instance, adding a "mango" to the fruitbasket you can do as follows:
##
fruitbasket = { "apple":3, "banana":5, "cherry":50 }
print( fruitbasket )
fruitbasket["mango"] = 1
print( fruitbasket )

