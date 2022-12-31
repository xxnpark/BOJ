cases = int(input())
for i in range(cases):
    line = input()
    point = 0
    score = 0
    for s in line:
        if s == "O" : point += 1
        else : point = 0
        score += point
    print(score)