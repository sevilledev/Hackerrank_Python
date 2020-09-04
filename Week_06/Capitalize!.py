def solve(s):
    list1 = list(s)
    t = len(list1)
    list1[0] = list1[0].upper()
    
    for i in range(t):
        if list1[i] == " ":
            list1[i+1] = list1[i+1].upper()
            
    s = ''.join(list1)
    return s


s = input()
result = solve(s)
print(result)
