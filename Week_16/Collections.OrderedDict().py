# Hackos : 20
from collections import OrderedDict

n = int(input())
list1 = [] 
ordereddict = OrderedDict()
for i in range (n):
    A = list(map(str, input().split()))
    name = ' '
    name = name.join(A[:-1])
    value = int(A[-1])
    if name not in list1:
        list1.append(name)
        ordereddict[name] = value
    else :
        newvalue = ordereddict[name] + value
        ordereddict.update({name : newvalue}) 
        
for k, v in ordereddict.items():
    print (k, v)
