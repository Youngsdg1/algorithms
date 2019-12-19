import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
ordered_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for test_case in range(1, T+1):
    case_length = int(input().split()[1])
    unordered_str = list(input().split())
    result = []

    for i in range(len(ordered_str)):
        for j in range(case_length):

            result.append(unordered_str[i])
    print('#{}'.format(test_case))
    print(' '.join(result))