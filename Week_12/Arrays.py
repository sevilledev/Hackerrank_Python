# Hackos : 20
import numpy

def arrays(arr):
    a = numpy.array(arr, float)
    b = a[::-1] 
    return b

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
