a, b = input(), input()
blist = [int(a) * int(i) for i in reversed(list(b))]
for num in blist : print(num)
print(int(a) * int(b))