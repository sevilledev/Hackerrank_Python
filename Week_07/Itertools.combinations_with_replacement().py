from itertools import combinations_with_replacement

a,b=input().split()
a=list(a)
a.sort()
s=list(combinations_with_replacement(a,int(b)))
for i in s:
    t = ''.join(i)
    print(t)
