# Harsh Tamakuwala
#662282
# ICS4U0
# Source txt wordcount
# Mr Veera
# march 19,2021
count=0
words=''
file=open('source.txt', 'r')
string=file.read()
words=(string.split(' '))
count=len(words)

total=0
for index in words:
    total+=(len(index))

average=total/count

file.close()

print(words)
print('number of words: ', count)
print(f'Average letters: {average:.2f}')
