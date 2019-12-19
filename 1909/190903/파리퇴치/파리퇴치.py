import sys
sys.stdin = open('pari.txt', 'r')
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())  # N*N 행렬, M*M 파리채
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = []
    s = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            for p in range(m):
                for q in range(m):
                    s += arr[i+p][j+q]
            res.append(s)
            s = 0
    print('#{} {}'.format(tc, max(res)))
