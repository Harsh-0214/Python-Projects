# Lesson Dictionary functions
# Mr Veera
# 26 Nov 2019

fruitbasket1 = { "apple":3, "banana":5, "cherry":50 }
##print( list( fruitbasket.keys() ) )
#print( list( fruitbasket.values() ) )
print( list( fruitbasket1.items() ) )
##

fruitbasket2 = { "apple":3, "apple":5, "cherry":50, "durian":0, "mango":2 }

for key in fruitbasket2.keys():
    print( list( fruitbasket2.items() ) )
    print( "{}:{}".format( key , fruitbasket2[key] ) )
    print( sum( fruitbasket2.values() ) )
