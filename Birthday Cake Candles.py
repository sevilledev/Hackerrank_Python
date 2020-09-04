def birthdayCakeCandles(ar):
    k=0
    max_number=ar[0]
    for i in range(len(ar)):
        if ar[i]>max_number:
            max_number=ar[i]
        else:
            pass
    for i in range(len(ar)):
        if ar[i]==max_number:
            k+=1
        else:
            pass
    return k
    
if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    
    print(result)
