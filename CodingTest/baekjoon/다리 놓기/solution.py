import sys
input = sys.stdin.readline

def cal_combination(n, m):
    numerator = 1
    for i in range(m, m-n, -1):
        numerator *= i

    denominator = 1
    for i in range(n, 1, -1):
        denominator *= i
    return int(numerator/denominator)

T = int(input())
for _ in range(T):
    n, m  = list(map(int, input().split()))
    answer = cal_combination(n, m)
    print(answer)