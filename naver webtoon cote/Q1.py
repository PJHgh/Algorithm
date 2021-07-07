from collections import Counter

def solution(S, pattern):
    answer = 0
    p = Counter(pattern)
    for i in range(len(S)-len(pattern)+1):
        s = S[i:i+len(pattern)]
        if Counter(s) == p:
            answer += 1
    return answer