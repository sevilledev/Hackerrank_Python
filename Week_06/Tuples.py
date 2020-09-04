n = int(input())
integer_list = map(int, input().split())
tuple1 = tuple(integer_list)

print(hash(tuple1))
