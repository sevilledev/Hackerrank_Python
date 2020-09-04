n=int(input())
for i in range(n):
    m = int(input())
    A = set(map(int,input().split()))
    n = int(input())
    B = set(map(int,input().split()))
    
    if A.intersection(B)==A :
        print("True") 
    else:
        print("False")
        
