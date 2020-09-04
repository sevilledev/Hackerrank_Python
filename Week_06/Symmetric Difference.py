n=int(input())
lis1=input().split()
m=int(input())
lis2=input().split()

a = list(map(int, lis1))
b = list(map(int, lis2))

x = set(a)
y = set(b)

x1=x.difference(y)
y1=y.difference(x)
x1.update(y1)
x1=list(x1)
x1.sort()

for i in x1:
    print(i)
