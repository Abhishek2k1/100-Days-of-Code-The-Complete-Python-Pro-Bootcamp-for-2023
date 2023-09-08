student_score = input("Input a list of student heights \n").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

highestScore=0
for score in student_score:
    if score>highestScore:
        highestScore=score
print(highestScore)
