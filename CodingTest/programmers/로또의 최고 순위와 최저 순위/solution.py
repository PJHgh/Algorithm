def solution(lottos, win_nums):
    n = lottos.count(0)
    m = len(set(lottos) & set(win_nums))
    rank = [6, 6, 5, 4, 3, 2, 1]
    answer = [rank[n+m], rank[m]]
    return answer