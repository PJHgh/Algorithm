def f(x):
    binx = bin(x)[2:]
    if binx[-1] == '0':
        binx = list(binx)
        binx[-1] = '1'
        binx = ''.join(binx)
        binx = binx[::-1]
    else:
        binx = binx[::-1]+'0'
        binx = list(binx)
        idx = binx.index('0')
        binx[idx-1], binx[idx] = '0', '1'
        binx = ''.join(binx)
    return sum([2**i*int(x) for i, x in enumerate(binx)])

def solution(numbers):
    return [f(number) for number in numbers]