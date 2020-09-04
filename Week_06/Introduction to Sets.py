def average(arr):
    s=0
    set1=set(arr)
    
    for i in set1:
        s=s+i
        
    return s/len(set1)


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
