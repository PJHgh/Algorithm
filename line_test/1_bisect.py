'''
문제 설명
int로 구성된 param0 이라는 list가 주어짐.
list의 일부만 정렬해도, list 전체가 정렬될 수 있음.
list 전체가 정렬되도록 하는 범위를 index 값으로 반환할 것.
'''

import heapq

def solution(param0: list) -> tuple:
    answer = []
    param1 = param0.copy()
    heapq.heapify(param1)
    for i, p0 in enumerate(param0):
        p1 = heapq.heappop(param1)
        if p0 != p1:
            answer.append(i)
    return answer[0], answer[-1]

print(solution([3,2,4,2,15,12,9,16,18,19]))
print(solution([1,2,4,7,10,11,7,12,6,7,16,18,19]))
print(solution([0,3,2,1,4,5,6,3,4,10,11,12]))
print(solution([0,1,1,1,1,2,1,3,1,9]))
print(solution([1,0]))
print(solution([1,3,4,2,5,6]))