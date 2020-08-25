integer_list = map(int, input().split())
integer_list = list(integer_list)
n = int(integer_list[0])
m = int(integer_list[1])
for i in range(1, n//2+1):
    print("-"*((m-(3*(2*(i-1)+1)))//2)+".|." *
          (2*(i-1)+1)+"-"*((m-(3*(2*(i-1)+1)))//2))
print("-"*((m-7)//2)+"WELCOME"+"-"*((m-7)//2))
for i in range(n//2, 0, -1):
    print("-"*((m-(3*(2*(i-1)+1)))//2)+".|." *
          (2*(i-1)+1)+"-"*((m-(3*(2*(i-1)+1)))//2))
