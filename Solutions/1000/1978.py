N = int(input())
num_list = list(map(int, input().split()))

def is_prime(n):
    if n == 1:
        return False
    for m in range(2, int(n**(1/2))+1):
        if n % m == 0:
            return False
    return True

print(sum([int(is_prime(n)) for n in num_list]))
