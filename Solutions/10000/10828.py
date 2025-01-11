def push(stack, x):
    stack.append(x)


def pop(stack):
    if len(stack) == 0:
        return -1
    return stack.pop()


def size(stack):
    return len(stack)


def empty(stack):
    return int(len(stack) == 0)


def top(stack):
    if len(stack) == 0:
        return -1
    return stack[-1]


stack = []
n = int(input())
for _ in range(n):
    instruct, *value = input().split()
    if instruct == "push":
        push(stack, int(value[0]))
    elif instruct == "pop":
        print(pop(stack))
    elif instruct == "size":
        print(size(stack))
    elif instruct == "empty":
        print(empty(stack))
    elif instruct == "top":
        print(top(stack))
