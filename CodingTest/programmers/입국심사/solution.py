def solution(n, times):
    if len(times) == 1:
        return times[0]*n
    
    num = -1
    min_time = 0
    max_time = n//len(times)*max(times)
    while max_time > min_time:
        mid_time = (max_time + min_time)//2
        num = sum(map(lambda x:mid_time//x, times))
        if num >= n:
            max_time = mid_time
        elif num < n:
            min_time = mid_time+1
    return max_time