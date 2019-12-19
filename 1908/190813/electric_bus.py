import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    stop = list(map(int, input().split()))
    stop_list = [0] * (n+1)

    for i in range(len(stop)):
        stop_list[stop[i]] += 1

    start = 0
    end = k
    ans = 0

    while True:
        zero = 0
        for i in range(start+1, end+1):
            if stop_list[i] == 1:
                start = i
            else:
                zero += 1

        if zero == k:
            ans = 0
            break

        ans += 1
        end = start + k

        if end >=n:
            break

    print('#{} {}'.format(test_case, ans))


