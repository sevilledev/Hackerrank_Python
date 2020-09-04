m, n = map(int, input().split())
X=[]

for i in range(n):
    arr = list(map(float, input().split()))
    X.append(arr)
    
for i in zip(*X):
    print(sum(i)/len(i))
