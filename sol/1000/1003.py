zero = [1, 0, 1]
one = [0, 1, 1]

def fib(n) :
    while len(zero) < n + 1 :
        length = len(zero)
        zero.append(zero[length - 2] + zero[length - 1])
        one.append(one[length - 2] + one[length - 1])
    print("%d %d" %(zero[n], one[n]))

cases = int(input())

for i in range(cases) :
    num = int(input())
    fib(num)