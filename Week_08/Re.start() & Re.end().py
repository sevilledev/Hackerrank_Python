s = input()
k = input()
v = len(s)
t = len(k)
match = 0

for i in range (0, v-t+1):
    if k == s[i:i+t]:
        print((i, i+t-1))
        match += 1

if match == 0:
    print((-1, -1))
    
