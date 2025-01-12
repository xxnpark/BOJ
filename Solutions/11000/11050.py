n, c = map(int, input().split())
ret = 1
for i in range(n, n - c, -1):
    ret *= i
for i in range(1, c + 1):
    ret //= i
print(ret)
