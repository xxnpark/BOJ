def push(queue, x):
    queue.append(x)


def pop(queue):
    if len(queue) == 0:
        return -1
    return queue.pop(0)


def size(queue):
    return len(queue)


def empty(queue):
    return int(len(queue) == 0)


def front(queue):
    if len(queue) == 0:
        return -1
    return queue[0]


def back(queue):
    if len(queue) == 0:
        return -1
    return queue[-1]


queue = []
n = int(input())
for _ in range(n):
    instruct, *value = input().split()
    if instruct == "push":
        push(queue, int(value[0]))
    elif instruct == "pop":
        print(pop(queue))
    elif instruct == "size":
        print(size(queue))
    elif instruct == "empty":
        print(empty(queue))
    elif instruct == "front":
        print(front(queue))
    elif instruct == "back":
        print(back(queue))
