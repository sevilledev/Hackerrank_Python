import math
import cmath

z = complex(input())
a = math.sqrt(z.real**2 + z.imag**2)
b = cmath.phase(complex(z.real, z.imag))

print (a)
print (b)
