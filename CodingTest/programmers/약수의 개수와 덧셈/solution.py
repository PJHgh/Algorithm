import math

def get_prime(n):
    lst = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if lst[i] == True:
            j = 2
            while i * j <= n:
                lst[i * j] = False
                j += 1
    return [i for i in range(2, n+1) if lst[i]]

def get_divisor(n):
    prime = get_prime(n)
    d = 1
    for p in prime:
        count = 0
        while n%p == 0:
            count += 1
            n /= p
        d *= count+1
    return d

def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        divisor = get_divisor(n)
        if divisor%2 == 0:
            answer += n
        else:
            answer -= n
    return answer