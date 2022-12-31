from collections import deque

INF = int(1e9)


def find_dist(graph, start, end, size, N):  # BFS
    q = deque([start])
    dist_list = [INF] * (N * N)
    dist_list[start[0] * N + start[1]] = 0
    direc_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while q:
        curr_x, curr_y = q.popleft()
        for direc in direc_list:
            new_x = curr_x + direc[0]
            new_y = curr_y + direc[1]
            if 0 <= new_x < N and 0 <= new_y < N and graph[new_x][new_y] <= size and dist_list[new_x * N + new_y] == INF:
                dist_list[new_x * N + new_y] = dist_list[curr_x * N + curr_y] + 1
                q.append((new_x, new_y))
    return dist_list[end[0] * N + end[1]]


N = int(input())

graph = [] * N
x = y = -1

for i in range(N):
    inpt = list(map(int, input().split()))
    graph.append(inpt)
    for j in range(N):
        if inpt[j] == 9:
            x = i
            y = j

size = 2
eat = 0
time = 0

while True:
    min_dist = INF
    min_x = min_y = N

    for i in range(N):
        for j in range(N):
            if 0 < graph[i][j] < min(size, 7):
                dist = find_dist(graph, (x, y), (i, j), size, N)
                if dist < min_dist or dist == min_dist and (i < min_x or i == min_x and j < min_y):
                    min_dist = dist
                    min_x = i
                    min_y = j
    
    if min_dist != INF:
        graph[x][y] = 0
        x = min_x
        y = min_y
        graph[x][y] = 9
        eat += 1
        time += min_dist
    else:
        break
    
    if eat == size:
        eat = 0
        size += 1

print(time)
