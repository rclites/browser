n = int(input())

my_stack = [input() for i in range(n)]

while my_stack:
    print(my_stack.pop())
