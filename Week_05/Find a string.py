def count_substring(string, sub_string):
    k=0
    t=len(sub_string)
    for i in range(0,len(string)):
        if string[i:i+t]==sub_string:
            k+=1
        else:
            pass

    return k


string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)
