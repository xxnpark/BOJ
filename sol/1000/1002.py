num = int(input())
for i in range(num):
    x1, y1, r1, x2, y2, r2 = [int(s) for s in input().split()]
    dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**(1/2)
    rsum = r1 + r2
    rsub = abs(r1 - r2)
    if dis == rsub == 0 : print(-1)
    elif dis > rsum : print(0)
    elif dis == rsum : print(1)
    elif dis < rsum :
        if dis > rsub : print(2)
        if dis == rsub : print(1)
        elif dis < rsub : print(0)