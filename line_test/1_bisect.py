'''
문제 설명
int로 구성된 param0 이라는 list가 주어짐.
list의 일부만 정렬해도, list 전체가 정렬될 수 있음.
list 전체가 정렬되도록 하는 범위를 index 값으로 반환할 것.
'''

import bisect

def solution(param0: list) -> tuple:
    # 순서를 유지하며, index와 값을 저장하는 list 초기화
    num_lst = []
    idx_lst = []
    # 가장 큰 값을 저장하는 변수 초기화
    past_max_num = float('-inf')
    # target 변수 초기화
    start_position, end_position = len(param0), len(param0)

    # 주어진 list 순회
    for idx, num in enumerate(param0):
        # 과거 값보다 크거나 같은 경우, list에 append 및 최대값 갱신
        if past_max_num <= num:
            num_lst.append(num)
            idx_lst.append(idx)
            past_max_num = num
        # 과거 값보다 작은 경우, 정렬해야 하는 범위를 탐색
        else:
            # 현재 위치를 포함하여 범위 지정
            end_position = idx
            # 저장된 list는 정렬되어 있으므로, 이진탐색을 통해 위치 파악
            lst_in_idx = bisect.bisect_right(num_lst, num)
            # 예외처리를 포함하여, start_position 저장
            start_position = min(start_position, idx_lst[lst_in_idx] if len(idx_lst) != lst_in_idx else end_position)
            # 정렬된 범위만 남도록 list를 갱신
            num_lst = num_lst[:lst_in_idx]
            idx_lst = idx_lst[:lst_in_idx]

    return start_position, end_position

# print(solution([3, 2, 4, 2, 15, 12, 9, 16, 18, 19]))
# print(solution([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
# print(solution([0,3,2,1,4,5,6,3,4,10,11,12]))
# print(solution([0,1,1,1,1,2,1,3,1,9]))
# print(solution([0]))
# print(solution([1,3,4,2,5,6]))