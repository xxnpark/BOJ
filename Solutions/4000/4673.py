def d(n: int):
    return n + sum(map(int, list(str(n))))

numlist = list(range(1, 10001))
for n in range(10000):
    try:
        numlist.remove(d(n))
    except:
        pass

for n in numlist : print(n)