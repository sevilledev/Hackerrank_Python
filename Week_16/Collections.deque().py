# Hackos : 20
from collections import deque
d = deque()

n = int(input())

for i in range (n):
    command = list(input().split())
    if command[0] == "append":
        d.append(command[1])
    elif command[0] == "appendleft":
        d.appendleft(command[1])
    elif command[0] == "pop":
        d.pop()
    elif command[0] == "popleft":
        d.popleft()
        
for i in d:
    print(i, end=' ')
