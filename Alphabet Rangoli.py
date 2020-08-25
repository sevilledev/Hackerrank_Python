def print_rangoli(n):
    list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    list2=list1[0:n]
    for i in range(n-1):
        print ("-"*((2*n-2)-2*i),end="")
        for x in range(1,i+2):
            print(f"{list2[-(x)]}-",end="")
        if i>=1:
            print(list2[-i],end="")
            for x in range(i-1,0,-1):
                print(f"-{list2[-(x)]}",end="")
            print("-"*((2*n-2)-2*i))
        else:
            print("-"*(((2*n-2)-2*i)-1))

    for i in range(1,n):
        print (f"{list2[-i]}-",end="")
    print("a",end="")
    for i in range(1,n):
        print (f"-{list2[i]}",end="")
    print()

    for i in range(n-2,-1,-1):
        print ("-"*((2*n-2)-2*i),end="")
        for x in range(1,i+2):
            print(f"{list2[-(x)]}-",end="")
        if i>=1:
            print(list2[-i],end="")
            for x in range(i-1,0,-1):
                print(f"-{list2[-(x)]}",end="")
            print("-"*((2*n-2)-2*i))
        else:
            print("-"*(((2*n-2)-2*i)-1))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
