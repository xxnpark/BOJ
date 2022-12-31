INF = int(1e9)


def floyd_warshall(graph, n):  # graph[a][b] = c : a에서 b로 가는 비용은 c, n : 노드 수
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
