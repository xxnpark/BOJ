def score(board, start):
    temp_score = sum(
        [sum(line[start[1] : start[1] + 8]) for line in board[start[0] : start[0] + 8]]
    )
    return min(temp_score, 64 - temp_score)


n, m = map(int, input().split())

board = []
for i in range(n):
    ipt = input()
    line = []
    for j, x in enumerate(ipt):
        if (i + j) % 2 == 0 and x == "W" or (i + j) % 2 == 1 and x == "B":
            line.append(1)
        else:
            line.append(0)
    board.append(line)

min_score = 64
for i in range(n - 7):
    for j in range(m - 7):
        min_score = min(min_score, score(board, (i, j)))

print(min_score)
