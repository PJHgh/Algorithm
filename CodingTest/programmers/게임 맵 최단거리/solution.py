import heapq

def dijkstra(start, n, m, graph):
    distance = [1e9 for _ in range(n*m)]
    distance[start] = 1
    q = []
    heapq.heappush(q, (1, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        cost = dist + 1
        for i in graph[now]:
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    return distance[-1]
    
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    graph = []
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 0:
                graph.append([])
                continue
            else:
                tmp = []
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if y+dy>=0 and y+dy<n and x+dx>=0 and x+dx<m and maps[y+dy][x+dx] == 1:
                        tmp.append((y+dy)*m+x+dx)
                graph.append(tmp)

    answer = dijkstra(0, n, m, graph)
    if answer == 1e9:
        return -1
    else:
        return answer