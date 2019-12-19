import sys
sys.stdin = open('pascal.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*10 for i in range(10)]
    for i in range(n):
        arr[i][0] = 1
        arr[i][i] = 1
        for j in range(i-1):
            arr[i][j+1] = arr[i-1][j]+arr[i-1][j+1]
    for i in range(10):
        while 0 in arr[i]:
            arr[i].remove(0)
    print('#{}'.format(tc))