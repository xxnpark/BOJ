def is_prime(n):
    if n == 1:
        return False
    for m in range(2, int(n**(1/2))+1):
        if n % m == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0 :
        break

    count = 0
    for n in range(n + 1, 2 * n + 1):
        if is_prime(n):
            count += 1
    print(count)