cases = int(input())
for i in range(cases):
    scores = list(map(int, input().split()[1:]))
    avg = sum(scores) / len(scores)
    n = 0
    for s in scores:
        if s > avg : n += 1
    print("%.3f%%" %(n/len(scores)*100))