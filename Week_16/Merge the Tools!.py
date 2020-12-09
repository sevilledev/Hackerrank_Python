# Hackos : 40
def convert(string): 
    result = []
    for c in string:
        if c not in result:
            result.append(c)
    result = ''.join(result)
    return result

def merge_the_tools(string, k):
    for i in range (0, len(string), k):
        v = string[i:i+k]
        mainstr = convert(v)
        print(mainstr) 

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
