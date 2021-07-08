'''
문제 설명
숫자 N에 대해서, 소인수 분해 표현식과 약수의 갯수를 반환할 것.
소인수 분해 표현식의 예시는 다음과 같음.
ex1) 12 = 2^2 * 3^1
ex2) 2 = 2^1
'''

import sys
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

line = sys.stdin.readline()

n = int(line)
primes = get_prime(n)

num = 1
form = []
for p in primes:
    d = 0
    while n%p == 0:
        d += 1
        n /= p
    if d > 0:
        num *= d+1
        form.append(str(p)+'^'+str(d))

print(num)
print(' * '.join(form))