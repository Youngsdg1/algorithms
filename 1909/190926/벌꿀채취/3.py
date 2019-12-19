import sys
sys.stdin = open('input.txt', 'r')
def subset(r, c):
    global M, C
    pass

def comb1(k, s):  # 조합 알고리즘 응용
    global mval
    profit = 0
    if k == 2:
        profit = bee[T[0]//N][T[0]%N] + bee[T[1]//N][T[1]%N]
        if profit > mval:
            mval = profit
        return
    else:
        for i in range(s, N*N-M+k):
            if i%N <= N-M:
                T[k] = A[i]
                comb1(k+1, i+M)

for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())  # N*N행렬, 벌통 개수 M, 최대 양 C
    data = [list(map(int, input().split())) for _ in range(N)]
    bee = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N-M-1):
            bee[i][j] = subset(i, j)
    #print(bee)
    mval = 0
    T = [0]*2
    A = [i for i in range(N*N-M+1)]
    comb1(0,0)
    print('#{} {}'.format(tc, mval))