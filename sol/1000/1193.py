def nsum(n):
    return int(n*(n+1)/2)

num = int(input())
n = 0
while nsum(n) < num:
    n += 1
seq = num - nsum(n-1)
if n % 2 == 1 : print(f"{n+1-seq}/{seq}")
else : print(f"{seq}/{n+1-seq}")