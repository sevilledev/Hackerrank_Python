import re
n = int(input())

for i in range(n): 
    line = input()
    z = re.findall(r".(#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3})",line) 
   
    if z:
        for i in z:
            print(i)
