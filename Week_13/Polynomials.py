# Hackos : 20
import numpy

A = list(map(float, input().split()))
x = int(input())

print (numpy.polyval(A, x))
