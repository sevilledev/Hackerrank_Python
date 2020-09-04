n,m = [int(x) for x in input().split()]
list1=[]

for i in range(n):
    x=input()
    list1.append(x)
    
for j in range(m):
    y=input()
    if y in list1:
        for i in range(len(list1)):
            if list1[i]==y:
                print(i+1,end=' ')
        print()
    else:
        print("-1")
