x=int(input())
list1 = list(map(int, input().rstrip().split()))
n=int(input())
sum=0
for i in range(n):
    a,b=[int(x) for x in input().split()] 
    if a in list1:
        sum += b
        list1.remove(a)
print(sum)
