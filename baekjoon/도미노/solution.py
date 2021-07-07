testcase = int(input())
for _ in range(testcase):
    n, m  = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        f, b  = list(map(int, input().split()))
        graph[b].append(f)
    print(graph)
    