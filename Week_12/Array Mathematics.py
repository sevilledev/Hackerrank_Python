# Hackos : 20
import numpy 

n, m = map(int, input().split())

a = numpy.zeros((n,m), int)
b = numpy.zeros((n,m), int)

for i in range(n):
  a[i] = numpy.array(input().split(), int)
for i in range(n): 
  b[i] = numpy.array(input().split(), int)  

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
