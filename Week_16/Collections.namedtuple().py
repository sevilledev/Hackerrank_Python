# Hackos : 20
from collections import namedtuple

n = int(input())
columns = input().split()

students = namedtuple('students', columns)
sum = 0
for i in range (n):
    x,y,z,t = input().split()
    student = students(x,y,z,t)
    sum += int(student.MARKS)
    
print(float("{:.2f}".format(sum/n)))
