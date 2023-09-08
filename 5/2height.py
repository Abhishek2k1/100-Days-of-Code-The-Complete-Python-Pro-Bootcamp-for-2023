student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = sum(student_heights)
no_of_student = len(student_heights)
avg = round(total_height/no_of_student)
print(avg)

totalheight= 0
for height in student_heights:
    totalheight+=height
print(totalheight)

numberOfStudent = 0
for Student in student_heights:
    numberOfStudent+=1
print(numberOfStudent)

print(round(totalheight/numberOfStudent))

