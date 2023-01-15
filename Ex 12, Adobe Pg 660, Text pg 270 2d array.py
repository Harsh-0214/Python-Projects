

#Student 1
print('Student 1: ')
s1t1=int(input('Test 1: '))
s1t2=int(input('Test 2: '))
s1t3=int(input('Test 3: '))
s1t4=int(input('Test 4: '))
s1t5=int(input('Test 5: '))

#Student 2
print('Student 2: ')
s2t1=int(input('Test 1: '))
s2t2=int(input('Test 2: '))
s2t3=int(input('Test 3: '))
s2t4=int(input('Test 4: '))
s2t5=int(input('Test 5: '))

#Student 3
print('Student 3: ')
s3t1=int(input('Test 1: '))
s3t2=int(input('Test 2: '))
s3t3=int(input('Test 3: '))
s3t4=int(input('Test 4: '))
s3t5=int(input('Test 5: '))

#Student 4
print('Student 4: ')
s4t1=int(input('Test 1: '))
s4t2=int(input('Test 2: '))
s4t3=int(input('Test 3: '))
s4t4=int(input('Test 4: '))
s4t5=int(input('Test 5: '))

#Student 5
print('Student 5: ')
s5t1=int(input('Test 1: '))
s5t2=int(input('Test 2: '))
s5t3=int(input('Test 3: '))
s5t4=int(input('Test 4: '))
s5t5=int(input('Test 5: '))
#Student 6
print('Student 6: ')
s6t1=int(input('Test 1: '))
s6t2=int(input('Test 2: '))
s6t3=int(input('Test 3: '))
s6t4=int(input('Test 4: '))
s6t5=int(input('Test 5: '))
#Student 7
print('Student 7: ')
s7t1=int(input('Test 1: '))
s7t2=int(input('Test 2: '))
s7t3=int(input('Test 3: '))
s7t4=int(input('Test 4: '))
s7t5=int(input('Test 5: '))
#Student 8
print('Student 8: ')
s8t1=int(input('Test 1: '))
s8t2=int(input('Test 2: '))
s8t3=int(input('Test 3: '))
s8t4=int(input('Test 4: '))
s8t5=int(input('Test 5: '))
#Student 9
print('Student 9: ')
s9t1=int(input('Test 1: '))
s9t2=int(input('Test 2: '))
s9t3=int(input('Test 3: '))
s9t4=int(input('Test 4: '))
s9t5=int(input('Test 5: '))
#Student 10
print('Student 10: ')
s10t1=int(input('Test 1: '))
s10t2=int(input('Test 2: '))
s10t3=int(input('Test 3: '))
s10t4=int(input('Test 4: '))
s10t5=int(input('Test 5: '))
#Student 11
print('Student 11: ')
s11t1=int(input('Test 1: '))
s11t2=int(input('Test 2: '))
s11t3=int(input('Test 3: '))
s11t4=int(input('Test 4: '))
s11t5=int(input('Test 5: '))
#Student 12
print('Student 12: ')
s12t1=int(input('Test 1: '))
s12t2=int(input('Test 2: '))
s12t3=int(input('Test 3: '))
s12t4=int(input('Test 4: '))
s12t5=int(input('Test 5: '))

#Averages for each student
as1=(s1t1+s1t2+s1t3+s1t4+s1t5)/5
as2=(s2t1+s2t2+s2t3+s2t4+s2t5)/5
as3=(s3t1+s3t2+s3t3+s3t4+s3t5)/5
as4=(s4t1+s4t2+s4t3+s4t4+s4t5)/5
as5=(s5t1+s5t2+s5t3+s5t4+s5t5)/5
as6=(s6t1+s6t2+s6t3+s6t4+s6t5)/5
as7=(s7t1+s7t2+s7t3+s7t4+s7t5)/5
as8=(s8t1+s8t2+s8t3+s8t4+s8t5)/5
as9=(s9t1+s9t2+s9t3+s9t4+s9t5)/5
as10=(s10t1+s10t2+s10t3+s10t4+s10t5)/5
as11=(s11t1+s11t2+s11t3+s11t4+s11t5)/5
as12=(s12t1+s12t2+s12t3+s12t4+s12t5)/5
classavg=(as1+as2+as3+as4+as5+as6+as7+as8+as9+as10+as11+as12)/12

#What will be in each row...
titles=['Names','Test 1','Test 2', 'Test 3', 'Test 4', 'Test 5', 'Averages']#top row
row1=['Student 1: ', s1t1,s1t2,s1t3,s1t4,s1t5,as1]
row2=['Student 2: ', s2t1,s2t2,s2t3,s2t4,s2t5,as2]
row3=['Student 3: ', s3t1,s3t2,s3t3,s3t4,s3t5,as3]
row4=['Student 4: ', s4t1,s4t2,s4t3,s4t4,s4t5,as4]
row5=['Student 5: ', s5t1,s5t2,s5t3,s5t4,s5t5,as5]
row6=['Student 6: ', s6t1,s6t2,s6t3,s6t4,s6t5,as6]
row7=['Student 7: ', s7t1,s7t2,s7t3,s7t4,s7t5,as7]
row8=['Student 8: ', s8t1,s8t2,s8t3,s8t4,s8t5,as8]
row9=['Student 9: ', s9t1,s9t2,s9t3,s9t4,s9t5,as9]
row10=['Student 10: ',s10t1,s10t2,s10t3,s10t4,s10t5,as10]
row11=['Student 11: ',s11t1,s11t2,s11t3,s11t4,s11t5,as11]
row12=['Student 12: ',s12t1,s12t2,s12t3,s12t4,s12t5,as12]

#Averages for each test
at1=(s1t1+s2t1+s3t1+s4t1+s5t1+s6t1+s7t1+s8t1+s9t1+s10t1+s11t1+s12t1)/12
at2=(s1t2+s2t2+s3t2+s4t2+s5t2+s6t2+s7t2+s8t2+s9t2+s10t2+s11t2+s12t2)/12
at3=(s1t3+s2t3+s3t3+s4t3+s5t3+s6t3+s7t3+s8t3+s9t3+s10t3+s11t3+s12t3)/12
at4=(s1t4+s2t4+s3t4+s4t4+s5t4+s6t4+s7t4+s8t4+s9t4+s10t4+s11t4+s12t4)/12
at5=(s1t5+s2t5+s3t5+s4t5+s5t5+s6t5+s7t5+s8t5+s9t5+s10t5+s11t5+s12t5)/12

#Last row
averages=['Averages: ',at1, at2, at3, at4, at5, classavg]
everything=[titles, row1, row2, row3, row4, row5, row6,row7,row8,row9,row10,row11,row12,averages]

#Printing
for i in range(len(everything)):
    for j in range(len(everything[i])):
        print(everything[i][j], end=' ')
    print()


