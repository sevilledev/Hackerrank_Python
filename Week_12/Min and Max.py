# Hackos : 20
import numpy

n, m = map(int, input().split())

a = numpy.zeros((n,m), int)

for i in range(n):
    a[i] = numpy.array(input().split(), int)
    
arr = numpy.min(a, axis = 1)
print (numpy.max(arr))
