numlist = [int(s[::-1]) for s in input().split()]
if numlist[0] > numlist[1] : print(numlist[0])
else : print(numlist[1])