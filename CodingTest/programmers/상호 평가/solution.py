def solution(scores):
    answer = ''
    for i, score in enumerate(map(list, zip(*scores))):
        my_score = score[i]
        if my_score == max(score) or my_score == min(score):
            if score.count(my_score) == 1:
                score.pop(i)
                
        mean_score = sum(score)/len(score)
        if mean_score >= 90:
            answer += 'A'
        elif mean_score >= 80:
            answer += 'B'
        elif mean_score >= 70:
            answer += 'C'
        elif mean_score >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer