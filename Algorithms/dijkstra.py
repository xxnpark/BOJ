import heapq
INF = int(1e9)


def dijkstra(start, graph, n):      # graph = [[(node2, cost12), (node3, cost13), ...], [...], ...], n : 노드 수
    distance = [INF] * n            # distance : 현재까지 각 노드의 최소거리 저장
    distance[start] = 0

    q = []                          # q : 현재 방문하지 않은 노드들의 최소거리 저장
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
