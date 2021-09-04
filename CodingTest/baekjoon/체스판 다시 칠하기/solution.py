import sys
input = sys.stdin.readline

n, m  = list(map(int, input().split()))
answer = 1e9
t1, t2 = [], []
for i in range(n):
    row = input()
    c1, c2 = [], []
    r1, r2 = [], []
    for j in range(m):
        if (i+j)%2 == 0 and row[j] == 'W':
            r1.append(1)
            r2.append(0)
        elif (i+j)%2 == 1 and row[j] == 'B':
            r1.append(1)
            r2.append(0)
        elif (i+j)%2 == 0 and row[j] == 'B':
            r1.append(0)
            r2.append(1)
        elif (i+j)%2 == 1 and row[j] == 'W':
            r1.append(0)
            r2.append(1)
        
        if j >= 7:
            c1.append(sum(r1))
            c2.append(sum(r2))
            r1.pop(0)
            r2.pop(0)

    t1.append(c1)
    t2.append(c2)
    if i >= 7:
        wstart = list(map(sum, zip(*t1)))
        bstart = list(map(sum, zip(*t2)))
        t1.pop(0)
        t2.pop(0)
        answer = min([answer]+wstart+bstart)
print(answer)

'''
echo "8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW" | python solution.py
'''