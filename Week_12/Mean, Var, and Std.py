# Hackos : 20
import numpy
numpy.set_printoptions(sign=' ')
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

A = numpy.zeros((n,m), int)

for i in range(n):
    A[i] = numpy.array(input().split(), int)

a = numpy.mean(A, axis = 1)
b = numpy.var(A, axis = 0)
c = numpy.std(A, axis = None)
    
print(a)
print(b)
print(c)
