import sys
sys.stdin = open('danjo.txt', 'r')
for tc in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))
    danjo = []
    for i in range(N):
        for j in range(i+1, N):
            danjo.append(A[i] * A[j])

    res = [0] * len(danjo)
    st_danjo = list(map(str, danjo))
    for i in range(0, len(st_danjo)):
        for j in range(len(st_danjo[i])-1):
            if not int(st_danjo[i][j]) < int(st_danjo[i][j+1]):
                break
            else:
                res[i] += 1

    real_res = []
    for i in range(len(danjo)):
        if len(st_danjo[i]) != 1 and len(st_danjo[i]) - res[i] == 1:
            real_res.append(danjo[i])

    if real_res == []:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, max(real_res)))
