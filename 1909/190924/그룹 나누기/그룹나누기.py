import sys
sys.stdin = open('input.txt', 'r')
def Find_set(x):
    if x == p[x]:
        return x
    else:
        return Find_set(p[x])
def Union(x, y):
    if Find_set(y) > Find_set(x):
        p[Find_set(y)] = Find_set(x)
    else:
        p[Find_set(x)] = Find_set(y)
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    p = [_ for _ in range(N)]  # 부모 노드 표시한거, 처음엔 자기 자신
    sinchungseo = list(map(int, input().split()))
    for i in range(0, 2*M, 2):
        Union(sinchungseo[i]-1, sinchungseo[i+1]-1)
    cnt = 0
    for i in range(N):
        if p[i] == i:
            cnt += 1
    print('#{} {}'.format(tc, cnt))