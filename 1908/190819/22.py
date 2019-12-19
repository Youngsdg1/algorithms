import sys
sys.stdin = open("input.txt", "r")
T = int(input())
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T + 1):
    first_line = list(input().split())
    test_case = list(input().split())
    res_num = []
    for i in test_case:
        res_num.append(nums.index(i))

    result = ""
    for j in range(10):
        result += res_num.count(j) * (nums[j] + " ")
    print('#{}'.format(tc))
    print('{}'.format(result))