def startpoint(n):
    if n == 0 : return 1
    elif n == 1 : return 2
    else : return startpoint(n-1) + 6*(n-1)

num = int(input())
n = 0
while startpoint(n) <= num:
    n += 1
print(n)