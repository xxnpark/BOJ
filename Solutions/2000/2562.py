numlist = []
for i in range(9):
    numlist.append(int(input()))
max = max(numlist)
print(max)
print(numlist.index(max) + 1)