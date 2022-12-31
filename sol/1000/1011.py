def s(n):
    return int(n*(n+1)/2 + n*(n-1)/2)

for r in range(int(input())):
    a, b = map(int, input().split())
    l = b - a
    n = 1
    while s(n) < l:
        n += 1
    if s(n) == l:
        print(n + n-1)
    else:
        if l - s(n-1) > n-1 : print(n-1 + n-2 + 2)
        else : print(n-1 + n-2 + 1)