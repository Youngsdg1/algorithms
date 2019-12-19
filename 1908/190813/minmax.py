import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    m = int(input())
    num_list = list(map(int, input().split()))
    result = max(num_list) - min(num_list)
    print('#{} {}'.format(T, result))

