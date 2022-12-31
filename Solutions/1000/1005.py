from collections import deque
import sys
input = sys.stdin.readline

cases = int(input())

for i in range(cases) :
    buildings, rules = [int(n) for n in input().split()]
    time = [int(n) for n in input().split()]
    rule = [[] for j in range(buildings)]
    incount = [0] * buildings
    maxtime = [0] * buildings
    
    for j in range(rules) :
        pre, post = [int(n) for n in input().split()]
        rule[pre - 1].append(post - 1)
        incount[post - 1] += 1

    seq = deque()

    for j in range(buildings) :
        if incount[j] == 0 :
           seq.append(j)
           maxtime[j] = time[j]
    while seq :
        out = seq.popleft()
        for n in rule[out] :
            incount[n] -= 1
            maxtime[n] = max(maxtime[out] + time[n], maxtime[n])
            if incount[n] == 0 :
                seq.append(n)
        
    final = int(input())
    print(maxtime[final - 1])