from itertools import combinations

def solution(places):
    answer = []
    for count, place in enumerate(places):
        pos = []
        for y, p in enumerate(place):
            pos.extend([(y, x) for x, s in enumerate(list(p)) if s == 'P'])
        if not pos:
            answer.append(1)
            continue
        
        positions = list(combinations(pos, 2))
        distance = list(map(lambda x:sum([abs(a-b) for a, b in zip(*x)]), positions))
        if 1 in distance:
            answer.append(0)
            continue
        
        distance = [i for i, d in enumerate(distance) if d == 2]
        for d in distance:
            pos1, pos2 = positions[d]
            pos1y, pos1x = pos1
            pos2y, pos2x = pos2
            if (pos1y+pos2y)%2 == 0 and place[(pos1y+pos2y)//2][(pos1x+pos2x)//2] != 'X':
                answer.append(0)
                break
            elif (pos1y+pos2y)%2 == 1 and place[pos1y][pos2x]+place[pos2y][pos1x] != 'XX':
                answer.append(0)
                break
        if len(answer) == count:
            answer.append(1)
    return answer