# Harsh Tamakuwala
# 662282
# Dictionaries intro ~ Coders Apprentice - 167
# ICS4U0
# Mr Veera
# April 07, 2021

##wordlist = ["apple","durian","banana","durian","apple","cherry","cherry","mango","apple","apple","cherry","durian","banana","apple","apple","apple","apple","banana","apple"]
##
##dictionary={}
##
##for key in wordlist:
##    if key in dictionary:
##        dictionary[key]+=1
##    else:
##        dictionary[key]=1
##
##print(dictionary)
##print()


dictionary={}

text = "apple ,durian ,banana ,durian ,apple ,cherry ,cherry ,mango ,apple ,apple ,cherry ,durian ,banana ,apple ,apple ,apple , apple ,banana ,apple"

temp=''
for index in text:
    print(text(index))
    if text(index)!=' ':
        temp+=text(index)
    elif text(index)!=',':
        temp+=text(index)
    else:
        dictionary[temp]+=1
        temp=''

print(dictionary)
    
print(text)
