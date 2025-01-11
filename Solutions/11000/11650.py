n = int(input())
ipts = [input().split() for _ in range(n)]
for ipt in sorted(ipts, key=lambda x: (int(x[0]), int(x[1]))):
    print(ipt[0], ipt[1])
