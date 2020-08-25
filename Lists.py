if __name__ == '__main__':
    n = int(input())
    list1 = []
    for x in range(n):
        command = input()
        if command[0:6] == "insert":
            command = command.split(" ")
            list1.insert(int(command[1]), int(command[2]))
        elif command == "print":
            print(list1)
        elif command[0:6] == "remove":
            command = command.split(" ")
            list1.remove(int(command[1]))
        elif command[0:6] == "append":
            command = command.split(" ")
            list1.append(int(command[1]))
        elif command == "sort":
            list1.sort()
        elif command == "pop":
            list1.pop()
        elif command == "reverse":
            list1.reverse()
