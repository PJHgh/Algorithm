def solution(enter, leave):
    n = len(enter)
    answer = [0 for _ in range(n)]
    room = []
    while leave:
        i = leave.pop(0)
        if i in room:
            room.remove(i)
            continue
        
        while enter:
            j = enter.pop(0)
            answer[j-1] += len(room)
            for k in room:
                answer[k-1] += 1
            room.append(j)
            if i == j:
                room.remove(i)
                break
    return answer