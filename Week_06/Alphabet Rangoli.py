import string


def print_rangoli(n):
    list1 = string.ascii_lowercase
    list2 = list1[0:n]

    # outputun [1;n-1]ci setirleri
    for i in range(n-1):
        print("-"*((2*n-2)-2*i), end="")
        for x in range(1, i+2):
            print(f"{list2[-(x)]}-", end="")
        if i >= 1:
            print(list2[-i], end="")
            for x in range(i-1, 0, -1):
                print(f"-{list2[-(x)]}", end="")
            print("-"*((2*n-2)-2*i))
        else:
            print("-"*(((2*n-2)-2*i)-1))

    # outputun n-ci setiri
    for i in range(1, n):
        print(f"{list2[-i]}-", end="")
    print("a", end="")
    for i in range(1, n):
        print(f"-{list2[i]}", end="")
    print()

    # outputun [n+1;2n]ci setirleri
    for i in range(n-2, -1, -1):
        print("-"*((2*n-2)-2*i), end="")
        for x in range(1, i+2):
            print(f"{list2[-(x)]}-", end="")
        if i >= 1:
            print(list2[-i], end="")
            for x in range(i-1, 0, -1):
                print(f"-{list2[-(x)]}", end="")
            print("-"*((2*n-2)-2*i))
        else:
            print("-"*(((2*n-2)-2*i)-1))


n = int(input())
print_rangoli(n)
