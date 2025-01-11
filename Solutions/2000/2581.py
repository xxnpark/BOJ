M = int(input())
N = int(input())

def is_prime(n):
    if n == 1:
        return False
    for m in range(2, int(n**(1/2))+1):
        if n % m == 0:
            return False
    return True

prime_list = []
for n in range(M, N+1):
    if is_prime(n):
        prime_list.append(n)

if not prime_list:
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])