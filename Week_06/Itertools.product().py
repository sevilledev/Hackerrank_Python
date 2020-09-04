from itertools import product

A=[int(x) for x in input().split()]
B=[int(y) for y in input().split()]

s=list(product(A,B))

for i in s:
    print(i,end=" ")
