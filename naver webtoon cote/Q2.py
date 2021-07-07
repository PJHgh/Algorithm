def solution(word):
    w2v = {k:v for v,k in enumerate(list('AEIOU'))}
    i2v = {'0':781, '1':156, '2':31, '3':6, '4':1}
    answer = 0
    for i, w in enumerate(word):
        answer += i2v[str(i)]*w2v[w]+1
    return answer