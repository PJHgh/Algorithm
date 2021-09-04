def solution(word):
    w2n = {w:n for n, w in enumerate('AEIOU')}
    i2n = {str(i):n for i, n in enumerate([781, 156, 31, 6, 1])}
    answer = sum([w2n[w]*i2n[str(i)]+1 for i, w in enumerate(word)])
    return answer