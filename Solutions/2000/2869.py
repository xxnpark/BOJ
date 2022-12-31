from math import ceil

a, b, c = map(int, input().split())
print(ceil((c-a)/(a-b))+1)

# (a-b)*(n-1)+a < c <= (a-b)*n+a
# (c-a)/(a-b) <= n < (c-a)/(a-b)+1