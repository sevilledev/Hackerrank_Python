# Hackos : 20
import numpy
numpy.set_printoptions(sign=' ')
numpy.set_printoptions(legacy='1.13')

A = list(map(float, input().split()))
arr = numpy.array(A)

print (numpy.floor(arr))
print (numpy.ceil(arr))
print (numpy.rint(arr))
