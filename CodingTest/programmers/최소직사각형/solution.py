def solution(sizes):
    sizes = list(map(sorted, sizes))
    a = sorted(sizes, key=lambda x:x[0])[-1][0]
    b = sorted(sizes, key=lambda x:x[1])[-1][1]
    return a*b