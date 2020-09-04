number = int(input())
students = []
students_name = []
students_score = []

for i in range(number):
    name = input()
    score = float(input())
    list1 = [name, score]
    students_score.append(score)
    students.append(list1)
    
students_score.sort()

for i in range(1, number):
    if students_score[i] > students_score[0]:
        t = students_score[i]
        break
        
for i in range(number):
    if students[i][1] == t:
        students_name.append(students[i][0])
        
students_name.sort()
for i in students_name:
    print(i)
    
