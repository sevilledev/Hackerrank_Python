def swap_case(s):
    list1 = list(s)
    for i in range(0, len(s)):
        a = list1[i].lower()
        b = list1[i].upper()
        if list1[i] == a:
            list1[i] = b
        else:
            list1[i] = a
    s = ''.join(list1)
    return s


s = input()
result = swap_case(s)
print(result)
