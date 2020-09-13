n = int(input())

for i in range(n):
    a, b = input().split()
    
    try:
        print(int(a)//int(b))
    except Exception as b:
        print("Error Code:",b)
        
