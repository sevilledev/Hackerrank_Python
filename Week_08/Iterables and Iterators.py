from itertools import combinations

n = int(input())
A = input().split()
k = int(input())
list1 = list(A)
list2 = []
for i in range(1, n+1):
    list2.append(i)
t = len(list(combinations(list2,k)))

for i in range(1,n+1):
    if list1[i-1] == "a":
        list2.remove(i)

v = len(list(combinations(list2,k)))
print("{0:.3}".format((t-v)/t))
