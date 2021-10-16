from itertools import combinations as combin

def intersect(lines):
    (A, B, E), (C, D, F) = lines
    if A*D - B*C == 0:
        return None
    else:
        x, y = (B*F-E*D)/(A*D-B*C), (E*C-A*F)/(A*D-B*C)
        if x%1 == 0 and y%1 == 0:
            return int(x), int(y)
        else:
            return None
    
def solution(line):
    intersect_points = [point for point in set(map(intersect, combin(line, 2))) if point != None]

    min_x = min(map(lambda x:x[0], intersect_points))
    min_y = min(map(lambda x:x[1], intersect_points))
    intersect_points = list(map(lambda x:(x[0]-min_x, x[1]-min_y), intersect_points))
    
    width = max(map(lambda x:x[0], intersect_points))+1
    height = max(map(lambda x:x[1], intersect_points))+1
    
    answer = []
    for i in range(height):
        tmp = list('.'*width)
        x_points = [point[0] for point in intersect_points if point[1] == i]
        for point in x_points:
            tmp[point] = '*'
        answer.append(''.join(tmp))
    return answer[::-1]