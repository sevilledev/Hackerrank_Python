n=int(input())

for i in range(n):
    m=input()
    
    if m.isdigit():
        m=int(m)
        k=0
        
        while m>=1:
            m=m/10
            k+=1
            
        m=int(m*10)
        
        if k==10 and (m==7 or m==8 or m==9):
            print("YES") 
        else:
            print("NO")
    else:
        print("NO")
