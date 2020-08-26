def diagonalDifference(arr):
    a=0
    b=0
    for i in range(n):
        a+=arr[i][i]
    for i in range(n):
        b+=arr[i][-(i+1)]
    c=abs(a-b)
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
