# Hackos : 20
import numpy

n, m, p = map(int, input().split())

A = numpy.zeros((n, p), int)
B = numpy.zeros((m, p), int)

for i in range(n):
    A[i] = numpy.array(input().split(), int) 
for i in range(m):
    B[i] = numpy.array(input().split(), int)
    
print (numpy.concatenate((A, B))) 
