import sys
sys.stdin = open('input.txt', 'r')
def find_parent(x, p):  # 더 큰 애 찾기
    global cnt
    queue = []
    visited = [0] * (N + 1)
    for ii in range(len(p[x])):
        queue.append(p[x][ii])  # x 보다 큰 것
        visited[p[x][ii]] = 1
        cnt += 1
    while queue:
        hing = queue.pop(0)
        for aa in p[hing]:  # 부모가 있으면
            if aa not in queue and not visited[aa]:
                queue.append(aa)
                visited[aa] = 1
                cnt += 1
    return


for tc in range(1, int(input()) + 1):
    N = int(input())
    M = int(input())
    pa = [[]*(N+1) for _ in range(N+1)]
    p_reverse = [[]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        pa[a].append(b)
        p_reverse[b].append(a)

    res = 0
    for idx in range(1, N+1):
        cnt = 0
        if pa:
            find_parent(idx, pa)
        if p_reverse:
            find_parent(idx, p_reverse)
        if cnt == N - 1:
            res += 1
    print('#{} {}'.format(tc, res))