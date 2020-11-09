# Hackos : 20
import numpy

n, m = map(int, input().split())

a = numpy.zeros((n,m), int)

for i in range(n):
  a[i] = numpy.array(input().split(), int) 

print (numpy.transpose(a))
print (a.flatten())
