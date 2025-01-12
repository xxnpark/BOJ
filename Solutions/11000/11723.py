import sys

input = sys.stdin.readline

m = int(input())
S = set()
for _ in range(m):
    instruct, *x = input().split()
    if not x:
        if instruct == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
        continue
    x = int(x[0])
    if instruct == "add":
        S.add(x)
    elif instruct == "remove":
        S.discard(x)
    elif instruct == "check":
        print(1 if x in S else 0)
    elif instruct == "toggle":
        if x in S:
            S.discard(x)
        else:
            S.add(x)
