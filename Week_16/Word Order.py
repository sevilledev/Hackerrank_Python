# Hackos : 50
from collections import OrderedDict

n = int(input())
ordereddict = OrderedDict()
for i in range (n):
    name = input()
    if name not in ordereddict.keys():
        ordereddict[name] = 1
    else :
        ordereddict[name] += 1

print(len(ordereddict))          
for v in ordereddict.values():
    print (v, end = ' ')
