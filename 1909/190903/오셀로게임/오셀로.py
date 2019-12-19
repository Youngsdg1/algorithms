import sys
sys.stdin = open('osello.txt', 'r')
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[0] * (n+1) for _ in range(n+1)]

    arr[len(arr) // 2][len(arr) // 2 + 1] = 1
    arr[len(arr) // 2 + 1][len(arr) // 2] = 1
    arr[len(arr) // 2][len(arr) // 2] = 2
    arr[len(arr) // 2 + 1][len(arr) // 2 + 1] = 2

    def find(arr, a, b, x, y):
        while True:
            a += x
            b += y
            if a > n or a < 0 or b > n or b < 0:
                return False
            else:
                if arr[a][b] == c:
                    return True
                elif arr[a][b] == 0:
                    return False

    def jjuk(arr, a, b, c):
        dx = [0, 0, -1, 1, 1, 1, -1, -1]
        dy = [-1, 1, 0, 0, -1, 1, -1, 1]
        origin_a = a
        origin_b = b
        for i in range(8):
            a = origin_a
            b = origin_b

            a += dx[i]
            b += dy[i]

            if a > n or a < 0 or b > n or b < 0:
                continue
            elif arr[a][b] != 0 and arr[a][b] != c:
                if find(arr, a, b, dx[i], dy[i]):
                    while arr[a][b] != c and arr[a][b] != 0:
                        arr[a][b] = c
                        a += dx[i]
                        b += dy[i]
                        if a > n or a < 0 or b > n or b < 0:
                            break

    for i in range(m):
        a, b, c = map(int, input().split())
        arr[a][b] = c
        jjuk(arr, a, b, c)

    print('#{} {} {}'.format(tc, sum(arr, []).count(1), sum(arr, []).count(2)))