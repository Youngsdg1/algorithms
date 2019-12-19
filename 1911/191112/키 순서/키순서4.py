import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def find_parent(x, p):  # 더 큰 애 찾기
    global path
    queue = deque()
    visited = [0] * (N + 1)
    for ii in range(len(p[x])):
        queue.append(p[x][ii])  # x 보다 큰 것
        path.append(p[x][ii])
        visited[p[x][ii]] = 1
    while queue:
        hing = queue.popleft()
        for aa in p[hing]:  # 부모가 있으면
            if aa not in queue and not visited[aa]:
                queue.append(aa)
                visited[aa] = 1
                if aa not in path:
                    path.append(aa)
    return

for tc in range(1, int(input()) + 1):
    N = int(input())
    M = int(input())
    # arr = deque(list(map(int, input().split())) for _ in range(M))
    pa = deque([]*(N+1) for _ in range(N+1))
    p_reverse = deque([]*(N+1) for _ in range(N+1))
    for _ in range(M):
        a, b = map(int, input().split())
        pa[a].append(b)
        p_reverse[b].append(a)
    print(pa)
    print(p_reverse)
    cnt = 0
    for idx in range(1, N+1):
        path = deque()
        if pa:
            find_parent(idx, pa)
        if p_reverse:
            find_parent(idx, p_reverse)
        if len(path) == N-1:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
