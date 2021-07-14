def solution(rows, columns, queries):
    maps = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(r*columns+c+1)
        maps.append(row)
    
    answer = []
    for query in queries:
        y1, x1, y2, x2 = query
        for y in range(y1-1, y2):
            if y == y1-1:
                tmp1, tmp2 = maps[y][x1-1], maps[y1][x1-1]
                min_tmp = min(tmp1, tmp2)
                for x in range(x1-1, x2):
                    if x == x2-1:
                        maps[y+1][x], tmp1 = tmp1, maps[y+1][x]
                    else:
                        maps[y][x+1], tmp1 = tmp1, maps[y][x+1]
                    min_tmp = min(tmp1, min_tmp)
            elif y == y2-1:
                for x in range(x1-1, x2):
                    if x == x2-1:
                        maps[y][x-1] = tmp1
                        maps[y1-1][x1-1] = tmp2
                    else:
                        maps[y][x] = maps[y][x+1]
                        min_tmp = min(maps[y][x+1], min_tmp)
            else:
                maps[y+1][x2-1], tmp1 = tmp1, maps[y+1][x2-1]
                maps[y][x1-1] = maps[y+1][x1-1]
                min_tmp = min(maps[y+1][x1-1], tmp1, min_tmp)
        answer.append(min_tmp)
    return answer