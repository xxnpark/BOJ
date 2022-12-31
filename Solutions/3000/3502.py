numlist = []
for i in range(10):
    numlist.append(int(input()) % 42)
print(len(set(numlist)))