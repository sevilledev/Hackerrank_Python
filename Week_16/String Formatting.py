# Hackos : 10
def print_formatted(number):
    m = len(bin(number)) - 2
    for i in range (1, number+1):
        print('{0:{m}d} {0:{m}o} {0:{m}X} {0:{m}b}'.format(i, m = m))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
