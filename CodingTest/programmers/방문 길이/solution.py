def solution(dirs):
    memory = set([])
    now_x, now_y = 0, 0
    answer = 0
    for d in dirs:
        if d == 'U':
            next_x, next_y = now_x, now_y+1
        elif d == 'L':
            next_x, next_y = now_x-1, now_y
        elif d == 'D':
            next_x, next_y = now_x, now_y-1
        else:
            next_x, next_y = now_x+1, now_y
        if next_x < -5 or next_x > 5 or next_y < -5 or next_y > 5:
            continue
        if not (now_x, now_y, next_x, next_y) in memory:
            memory.add((now_x, now_y, next_x, next_y))
            memory.add((next_x, next_y, now_x, now_y))
            answer += 1
        now_x, now_y = next_x, next_y
    return answer