m = int(input())
A = set(map(int,input().split()))
n = int(input())
B = set(map(int,input().split()))

C = A.union(B)
print(len(C))
