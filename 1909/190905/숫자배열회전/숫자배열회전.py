import sys
import time
sys.stdin = open('num.txt', 'r')
stime = time.time()
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res_arr = [[0] * n for _ in range(n)]

    x = 0
    res_1 = []
    for _ in range(n):
        for i in range(n-1, -1, -1):
            res_1.append(arr[i][x])
        x += 1

    y = 0
    res_2 = []
    for _ in range(n):
        for j in range(n-1, -1, -1):
            res_2.append(arr[n-y-1][j])
        y += 1

    z = n
    res_3 = []
    for _ in range(n):
        z -= 1
        for j in range(n):
            res_3.append(arr[j][z])

    k = 0
    result = res_1 + res_2 + res_3
    for i in range(n):
        for j in range(n):
            res_arr[j][i] = result[n*j+k:n*(j+1)+k]
        k += (n*n)

    Res = []
    for i in range(n):
        for j in range(n):
            Res.append(''.join(map(str, res_arr[i][j])))
    print('#{}'.format(tc))
    for i in range(0, n*n, n):
        print(' '.join(map(str, Res[i:i+n])))
    print(time.time()-stime)