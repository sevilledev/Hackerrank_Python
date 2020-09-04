def timeConversion(s):
    if s[8:10]=="AM":
        t=s[0:2]
        if t=="12":
            x="00"+s[2:8]
            return x
        else:
            x=s[0:8]
            return x
    else:
        t=s[0:2]
        if t=="12":
            x=s[0:8]
            return x
        else:
            t=str(int(t)+12)
            x=t+s[2:8]
            return x
    

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)
