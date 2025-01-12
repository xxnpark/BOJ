def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


a, b = map(int, input().split())

gcd = GCD(a, b)
print(GCD(a, b))
print(a * b // gcd)
