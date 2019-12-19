import sys
sys.stdin = open('dana.txt', 'r')
for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split()))+[0] for _ in range(n)] + [[0] * (n+1)]
    ans = 0
    for i in range(n):
        row_cnt = 0
        for j in range(n):
            if arr[i][j] == 0:
                row_cnt = 0
            elif arr[i][j] == 1:
                row_cnt += 1
                if row_cnt == k and arr[i][j+1] == 0:
                    ans += 1
    for j in range(n):
        col_cnt = 0
        for i in range(n):
            if arr[i][j] == 0:
                col_cnt = 0
            elif arr[i][j] == 1:
                col_cnt += 1
                if col_cnt == k and arr[i+1][j] == 0:
                    ans += 1
    print('#{} {}'.format(tc, ans))