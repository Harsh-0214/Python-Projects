student_number=int(input('give number of students: '))
number_tests= int(input('give number of tests: '))

entries=[]
for value in range(student_number):
    student=[]
    entries.append(student)
    for test in range(number_tests):
        entries[value].append(int(input("{} {}{}".format("give marks for student ",((str(value+1)),": ")))))
print(entries)
                                  
