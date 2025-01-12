import sys

input = sys.stdin.readline

n = int(input())
sol = [0]
for num in range(1, n):
    sol.append(sol[num - 1] + 1)
    if (num + 1) % 2 == 0:
        sol[num] = min(sol[num], sol[(num + 1) // 2 - 1] + 1)
    if (num + 1) % 3 == 0:
        sol[num] = min(sol[num], sol[(num + 1) // 3 - 1] + 1)
print(sol[-1])
