n = int(input())
s = set(map(int, input().split()))
m=int(input())
sum1=0

for i in range(m):
    command=input()
    
    if command=="pop":
        s.pop()
    elif command[0:6]=="remove":
        command=command.split(" ")
        s.remove(int(command[1]))
    elif command[0:7]=="discard":
        command=command.split(" ")
        s.discard(int(command[1]))
        
        
for i in s:
    sum1=sum1+int(i)
    
print(sum1)
