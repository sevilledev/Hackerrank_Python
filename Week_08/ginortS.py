string = input()
list1 = []
list2 = []
list3 = []
list4 = []

for i in string:
    if i.isalpha():
        if i.islower():
            list1.append(i)
        else:
            list2.append(i)
    else:
        if int(i)%2 == 1:
            list3.append(i)
        else:
            list4.append(i)
            
list1.sort()
list2.sort()
list3.sort()
list4.sort()

t = "".join(list1) + "".join(list2) + "".join(list3) + "".join(list4)
print (t)
