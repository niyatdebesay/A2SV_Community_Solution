if __name__ == '__main__':
    N = int(input())
    commands = {
    'insert': lambda args: my_list.insert(int(args[0]), int(args[1])),
    'print': lambda args: print(my_list),
    'remove': lambda args: my_list.remove(int(args[0])),
    'append': lambda args: my_list.append(int(args[0])),
    'sort': lambda args: my_list.sort(),
    'pop': lambda args: my_list.pop(),
    'reverse': lambda args: my_list.reverse()
}
my_list = []
for _ in range(N):
    cmd, *args= input().split()
    if cmd in commands:
        commands[cmd](args)
    else:
        print("Unknown Command ")
