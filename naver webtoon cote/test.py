from Q1 import solution as q1
from Q2 import solution as q2
from Q3 import solution as q3

# Q1
print('='*50)
print('Question 1')
print('-'*50)
S_list = ['abababaabaab']
pattern_list = ['aaab']
actual_list = [3]
for S, pattern, actual in zip(S_list, pattern_list, actual_list):
    expected = q1(S, pattern)
    if expected == actual:
        print(f'[TEST/SUCCESS] {expected} == {actual} !!')
    else:
        print(f'[TEST/FAILURE] {expected} != {actual} !!')

# Q2
print('='*50)
print('Question 2')
print('-'*50)
word_list = ['AEIOU', 'A']
actual_list = [245, 1]
for word, actual in zip(word_list, actual_list):
    expected = q2(word)
    if expected == actual:
        print(f'[TEST/SUCCESS] {expected} == {actual} !!')
    else:
        print(f'[TEST/FAILURE] {expected} != {actual} !!')

# Q2
print('='*50)
print('Question 3')
print('-'*50)
letters_list = ['yxzabc', 'yxzabcxy']
k_list = [3, 3]
actual_list = ['zbc', 'zxy']
for letters, k, actual in zip(letters_list, k_list, actual_list):
    expected = q3(letters, k)
    if expected == actual:
        print(f'[TEST/SUCCESS] {expected} == {actual} !!')
    else:
        print(f'[TEST/FAILURE] {expected} != {actual} !!')

