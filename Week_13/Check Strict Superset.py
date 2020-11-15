# Hackos : 10
A = set(map(int, input().split()))
n = int(input())
counter = 0

for i in range (n):
    B = set(map(int, input().split()))
    if A.issuperset(B):
        counter += 1

print(counter == n)
