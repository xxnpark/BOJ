n, k = map(int, input().split())
queue = [i for i in range(1, n + 1)]

ret = []
print("<", end="")
while len(queue) > 1:
    for i in range(k - 1):
        queue.append(queue.pop(0))
    print(queue.pop(0), end=", ")
print(queue[0], end=">")
