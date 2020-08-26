def miniMaxSum(arr):
    arr.sort()
    t=arr[0]+arr[1]+arr[2]+arr[3]
    d=arr[-4]+arr[-3]+arr[-2]+arr[-1]
    print(t,end=" ")
    print(d)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
