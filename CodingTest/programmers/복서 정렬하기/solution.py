def solution(weights, head2head):
    n = len(weights)
    sortkeys = []
    for i, (weight, head) in enumerate(zip(weights, head2head)):
        score = list(map(lambda x:1 if x == 'W' else 0, head))
        match_num = len([h for h in head if h != 'N'])
        if not match_num:
            key1 = 0
        else:
            key1 = -1*sum(score)/match_num
        key2 = -1*sum([s for w, s in zip(weights, score) if w > weight])
        sortkeys.append([key1, key2, -1*weight, i])
    sortkeys.sort(key=lambda x:(x[0], x[1], x[2], x[3]))
    
    answer = [i+1 for _, _, _, i in sortkeys]
    return answer