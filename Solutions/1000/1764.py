import sys

input = sys.stdin.readline

names = set()
n, m = map(int, input().split())
for _ in range(n):
    names.add(input().strip())

intersect_names = set()
for _ in range(m):
    if (name := input().strip()) in names:
        intersect_names.add(name)

print(len(intersect_names))
print("\n".join(sorted(intersect_names)))
