import math

a=int(input())
b=int(input())

c=(math.sqrt(a**2+b**2))/2
x=(b**2)/(2*b*c)
y=math.degrees(math.acos(x))

print(round(y),end='')
print('°')
