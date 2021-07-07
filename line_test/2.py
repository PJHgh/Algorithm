'''
문제 설명
숫자 N에 대해서, 소인수 분해 표현식과 약수의 갯수를 반환할 것.
소인수 분해 표현식의 예시는 다음과 같음.
ex1) 12 = 2^2 * 3^1
ex2) 2 = 2^1
'''

import sys
import math

def get_prime(n: int) -> list:
    ''' n까지의 소수를 구하는 에라스토테네스의 체 함수 '''
    # 각 index가 수를 표현하도록 list 초기화
    lst = [False]*2 + [True]*(n-1)

    # n의 제곱근을 포함하는 범위까지만 순회
    for i in range(math.ceil(math.sqrt(n))) :
        # list의 값이 True인 경우만 동작
        if lst[i] :
            j = 2
            # 해당 index의 배수인 모든 index는 False로 변환
            while i*j < n :
                lst[i*j] = False
                j += 1
    
    # index가 True인 모든 수를 list 형태로 반환
    return [i for i in range(len(lst)) if lst[i]==True]

def factorization(primes: list, n: int) -> list:
    ''' n의 소인수 분해 식을 만드는 함수 '''
    lst = []
    # n이하의 모든 소수를 순회
    for prime in primes:
        cnt = 0
        tmp = n
        # 해당 소수로 n을 몇 번 나눌 수 있는지 저장
        while True:
            q, r = divmod(tmp, prime)
            if r == 0:
                cnt += 1
                tmp = q
            else:
                break
        # 한 번 이상 나눠진 경우 list에 append
        if cnt > 0:
            lst.append((prime, cnt))
    return lst

def main(line: str) -> str:
    ''' 위 함수를 호출하는 main 함수 '''
    # 위 함수를 호출
    n = int(line)
    primes = get_prime(n)
    factorization_lst = factorization(primes, n)

    # 필요한 변수 초기화
    factorization_expression = []
    divisor_cnt = 1

    # 소인수 분해 식을 저장하고 있는 list를 순회
    for prime, cnt in factorization_lst:
        string = str(prime) + '^' + str(cnt)
        factorization_expression.append(string)
        divisor_cnt *= (cnt+1)

    # 약수의 갯수 및 소인수 분해 표현을 string 형태로 변환
    divisor_cnt = str(divisor_cnt)
    if len(factorization_expression) == 1:
        factorization_expression = factorization_expression[0]
    else:
        factorization_expression = ' * '.join(factorization_expression)
    return factorization_expression + '\n' + divisor_cnt

line = sys.stdin.readline()
print(main(line))