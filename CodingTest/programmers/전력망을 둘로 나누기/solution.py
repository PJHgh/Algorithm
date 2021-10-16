import copy
from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    answer = 1e9
    for v1, v2 in wires:
        _graph = copy.deepcopy(graph)
        _graph[v1].remove(v2)
        _graph[v2].remove(v1)
        
        visited = []
        q = deque([1])
        while q:
            s = q.pop()
            visited.append(s)
            for e in _graph[s]:
                if e in visited:
                    continue
                q.append(e)
        answer = min(answer, abs(2*len(visited)-n))
    return answer