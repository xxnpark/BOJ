def ifhan(n: int):
    numlist = list(map(int, list(str(n))))
    d = [numlist[i] - numlist[i+1] for i in range(len(numlist)-1)]
    if len(set(d)) <= 1 : return True
    else : return False

num = int(input())
count = 0
for i in range(1, num+1):
    if ifhan(i) : count += 1
print(count)