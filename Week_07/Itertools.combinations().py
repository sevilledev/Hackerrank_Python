from itertools import combinations

a,b=input().split()
b=int(b)
a=list(a)
a.sort()

for j in range(1,b+1):
    s=list(combinations(a,int(j)))
    for i in s:
        t = ''.join(i)
        print(t)
        
