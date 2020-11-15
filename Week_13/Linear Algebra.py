# Hackos : 20
import numpy

n = int(input())

A = numpy.zeros((n,n), float)

for i in range(n):
    A[i] = numpy.array(input().split(), float)

print (round(numpy.linalg.det(A), 2))
