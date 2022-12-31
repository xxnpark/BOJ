import copy

SHARK = 0
direc_list = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def eat(data_in, graph_in, curr_x, curr_y):
    data = copy.deepcopy(data_in)
    graph = copy.deepcopy(graph_in)

    eat_num = graph[curr_x][curr_y][0]
    data[eat_num] = None
    graph[curr_x][curr_y][0] = SHARK

    for n in range(1, 17):
        if not data[n]:
            continue
        x, y, direc = data[n]
        for k in range(8):
            dx, dy = direc_list[(direc + k) % 8]
            if 0 <= x + dx < 4 and 0 <= y + dy < 4 and (x + dx != curr_x or y + dy != curr_y):
                data[n] = (x + dx, y + dy, (direc + k) % 8)
                data[graph[x + dx][y + dy][0]] = (x, y, graph[x + dx][y + dy][1])
                graph[x][y] = graph[x + dx][y + dy]
                graph[x + dx][y + dy] = [n, (direc + k) % 8]
                break
    
    curr_direc = graph[curr_x][curr_y][1]
    dx, dy = direc_list[curr_direc]

    max_num = 0
    for k in range(1, 4):
        if 0 <= curr_x + dx * k < 4 and 0 <= curr_y + dy * k < 4 and 1 <= graph[curr_x + dx * k][curr_y + dy * k][0] <= 16:
            max_num = max(max_num, eat(data, graph, curr_x + dx * k, curr_y + dy * k))
    return eat_num + max_num


data_ = [None] * 17
graph_ = []
for i in range(4):
    inpt = list(map(int, input().split()))
    for j in range(4):
        data_[inpt[j * 2]] = (i, j, inpt[j * 2 + 1] - 1)
    graph_.append([[inpt[j * 2], inpt[j * 2 + 1] - 1] for j in range(4)])

print(eat(data_, graph_, 0, 0))
