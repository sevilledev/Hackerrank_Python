nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

list1 = []
for i in range(n):
    list1.append(arr[i][k])
    
list1.sort()
set1 = set(list1)

for i in set1:
    for j in range(n):
        if i == arr[j][k]:
            for t in arr[j]:
                print(t, end=" ")
            print()
