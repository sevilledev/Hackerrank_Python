n = int(input())
A = input().split()
for i in A :
    if int(i) <= 0:
        print("False")
        quit()

status = "False"
for i in A:
    if list(i) == list(reversed(list(i))):
        print("True")
        status = "True"
        break

if status == "False":
    print("False")
