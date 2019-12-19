# 완전검색으로 푸는데 가지치기 할 수 있는지 찾아보기
def perm(k, temp=100):
    global max
    if k == n:
        if temp > max:
            max = temp
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            if temp * data[k][arr[k]] > max:  # 가지치기
                perm(k+1, temp*data[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]

import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [ii for ii in range(n)]
    data = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            data[i][j] *= 0.01
    max = 0
    perm(0)
    round(max, 7)
    print("#{} {}".format(tc, "%0.6f"%max))