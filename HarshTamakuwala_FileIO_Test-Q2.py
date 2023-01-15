#Harsh Tamakuwala
#662282
#Mr.Veera
#File-I/O Test-straight road - Q2
#March 30, 2021

distance = input('Enter: ').split()
distance=[int(i) for i in distance]

file=open('input.txt', 'w')
file.read(str(distance))
file.close()


i=0

result=[]

while (i<len(distance)):
    row=[]
    d=0
    while (d<len(distance)):
        if d>i:
            row.append(distance[d] + row[d-1])
        elif i>d:
            row.append(result[d][i])
        else:
            row.append(0)

        d+=1

    result.append(row)
    i+=1

for row in result:
    print('The distance between the cities is: ', row)
