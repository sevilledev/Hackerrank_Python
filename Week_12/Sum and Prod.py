# Hackos : 20
import numpy

n, m = map(int, input().split())

a = numpy.zeros((n,m), int)

for i in range(n):
    a[i] = numpy.array(input().split(), int)

b = numpy.sum(a, axis = 0)
print (numpy.prod(b))
