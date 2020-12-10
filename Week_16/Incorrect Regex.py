# Hackos : 20
import re

n = int(input())

for i in range (n):
    regex = input()
    result = True
    
    try:
        reg = re.compile(regex)
    except re.error:
        result = False
    print (result)
