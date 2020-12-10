# Hackos : 10
from collections import Counter

k = int(input())
alllist = map(int, input().split())
roomList = Counter(alllist)

for k, v in roomList.items():
    if v == 1:
        print(k)
