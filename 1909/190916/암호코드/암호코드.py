import sys
sys.stdin = open('input.txt', 'r')
# XOR 연산 쓰기 ^
def find_right_bottom(arr, n, m):
    global password
    for i in range(n - 1, 0, -1):
        for j in range(m - 1, 0, -1):
            if arr[i][j] == 1:
                password = arr[i][j - 55:j + 1]
                return

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())  # 세로, 가로
    arr = [list(map(int, input())) for _ in range(n)]
    # 1 이 있는 인덱스 찾기 : for i in range(n): arr[i][::-1].find('1')
    code = [
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0 ,0, 1],
        [0, 0 ,1, 0, 0, 1, 1],
        [0, 1, 1 ,1 ,1 ,0 ,1],
        [0, 1, 0 ,0 ,0, 1 ,1],
        [0, 1, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 1 ,1, 1],
        [0, 1 ,1, 1 ,0, 1, 1],
        [0, 1 ,1 ,0, 1, 1 ,1],
        [0, 0, 0 ,1 ,0 ,1 ,1]
        ]
    find_right_bottom(arr, n, m)
    num = [0, 0, 0, 0 ,0, 0, 0, 0]
    a = 0
    for i in range(0, 56, 7):
        cd = password[i:i+7]
        num[a] = code.index(cd)
        a += 1
    if (((num[0] + num[2] + num[4] + num[6]) * 3) + (num[1] + num[3] + num[5]) + num[7]) % 10 == 0:
        print('#{} {}'.format(tc, sum(num)))
    else:
        print('#{} {}'.format(tc, 0))


