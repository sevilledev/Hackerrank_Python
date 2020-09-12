cube = lambda x: x**3  

def fibonacci(n):
    list1 = []
    a, b = 0, 1
    for i in range(n):
        list1.append(a)
        a, b = b, a+b
    return list1
    

n = int(input())
print(list(map(cube, fibonacci(n))))
    
