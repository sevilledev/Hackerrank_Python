n = int(input())
arr = map(int, input().split())
arr=list(arr)
maxeded=arr[0]

for eded in arr:
    if eded>maxeded:
        maxeded=eded
maxeded=maxeded-1

while maxeded not in arr:
    maxeded=maxeded-1
    
print(maxeded)
