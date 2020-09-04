from itertools import permutations

a,b=input().split()
a=list(a)
a.sort()
s=list(permutations(a,int(b)))
for i in s:
    t = ''.join(i)
    print(t)
    
