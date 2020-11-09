# Hackos : 20
import numpy

n = int(input())

a = numpy.zeros((n,n), int)
b = numpy.zeros((n,n), int)

for i in range(n):
  a[i] = numpy.array(input().split(), int)
for i in range(n): 
  b[i] = numpy.array(input().split(), int)

print(numpy.dot(a, b))
