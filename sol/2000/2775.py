for i in range(int(input())):
    k = int(input())
    n = int(input())
    apt = [[x for x in range(1, n+1)]]
    for f in range(k):
        temp = []
        for r in range(n):
            temp.append(sum(apt[f][:r+1]))
        apt.append(temp)
    print(apt[-1][-1])