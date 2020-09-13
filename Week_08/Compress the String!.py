s = input()
t = 1

for i in range(len(s)):
    if i != len(s)-1:
        if s[i] == s[i+1]:
            t += 1
        else:
            print((t,int(s[i])), end = " ")
            t = 1
    else:
        if s[i] != s[i-1]:
            t = 1
print((t,int(s[-1])), end = " ")
