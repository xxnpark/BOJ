input()
numlist = list(map(int, input().split()))
max = max(numlist)
numlist = list(map(lambda n : n / max * 100, numlist))
print(sum(numlist) / len(numlist))