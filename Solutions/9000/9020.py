def is_prime(n):
    if n == 1:
        return False
    for m in range(2, int(n**(1/2))+1):
        if n % m == 0:
            return False
    return True

T = int(input())

for i in range(T):
    n = int(input())
    m = int(n / 2)

    while m > 1:
        if is_prime(m) and is_prime(n - m):
            print(m, n - m)
            break
        m -= 1
