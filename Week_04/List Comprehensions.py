x = int(input())
y = int(input())
z = int(input())
n = int(input())
list=[]

for i in range(0,x+1):
    for t in range(0,y+1):
        for k in range (0,z+1):
            if (i+t+k)!=n :
                array=[i,t,k]
                list.append(array)
                
print (list)
