[A, B, C] = [int(s) for s in input().split()]
print("%d\n%d\n%d\n%d" %((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C))