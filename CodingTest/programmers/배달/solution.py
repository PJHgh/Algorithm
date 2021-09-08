import heapq

def dijkstra(start, N, graph):
    distance = [1e9 for _ in range(N+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    distance = dijkstra(1, N, graph)
    
    answer = sum([1 for d in distance[1:] if d <= K])
    return answer