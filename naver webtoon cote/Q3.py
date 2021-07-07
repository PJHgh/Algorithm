import heapq

def solution(letters, k):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    w2v = {k:v for v,k in enumerate(alphabet)}
    
    n = len(letters)
    q = [(-1*w2v[l], l, i) for i, l in enumerate(letters)]
    heapq.heapify(q)
    
    max_index = -1
    result = []
    while q:
        _, l, i = heapq.heappop(q)
        if max_index < i:
            max_index = i
            if max_index == n-1:
                max_index = -1
        else:
            continue
        result.append((i, l))
        if len(result) == k:
            break
    
    answer = ''
    heapq.heapify(result)
    while result:
        _, l = heapq.heappop(result)
        answer += l
    return answer