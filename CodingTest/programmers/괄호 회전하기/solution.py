def solution(s):
    rule_block = ['()', '[]', '{}']
    answer = 0
    for i in range(len(s)):
        ss = s[i:]+s[:i]
        while ss:
            now_ss = ss
            for block in rule_block:
                if block in ss:
                    ss = ''.join(ss.split(block))
            if now_ss == ss:
                break
        else:
            answer += 1
    return answer