import sys
import heapq
input = sys.stdin.readline

n = int(input())
pos_numbers  = list(map(int, input().split()))
neg_numbers  = list(map(lambda x:-1*x, pos_numbers))

heapq.heapify(neg_numbers)
heapq.heapify(pos_numbers)

min_num = heapq.heappop(pos_numbers)
max_num = heapq.heappop(neg_numbers)

answer = -1*min_num*max_num
print(answer)

'''
echo "2
4 2" | python solution.py
'''