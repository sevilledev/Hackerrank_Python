m = int(input())
A = set(map(int,input().split()))
n = int(input())
sum = 0

for i in range (n):
    command , x = input().split()
    B = set(map(int,input().split()))
    if command == "intersection_update":
        A.intersection_update(B)
    elif command == "update":
        A.update(B)
    elif command == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif command == "difference_update":        
        A.difference_update(B)
        
for j in A:
    sum += j
    
print (sum)
