# Hackos : 20
import numpy

A = list(map(int, input().split()))
my_array = numpy.array(A)
print (numpy.reshape(my_array,(3,3)))
