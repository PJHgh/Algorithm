def solution(table, languages, preference):
    languages = {l:p for l, p in zip(languages, preference)}
    
    answer = ''
    max_score = 0
    for job in table:
        job = job.split(' ')
        job2score = {j:5-i for i, j in enumerate(job[1:])}
        job = job[0]
        
        score = sum([p*job2score[l] for l, p in languages.items() if l in job2score.keys()])
        if max_score < score:
            answer = job
            max_score = score
        elif max_score == score:
            answer = sorted([answer, job])[0]
    return answer