import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def find_parent(x):  # 더 큰 애 찾기
    global upper_path
    queue = deque()
    visited = [0] * (N + 1)
    for ii in range(len(p[x])):
        queue.append(p[x][ii])  # x 보다 큰 것
        upper_path.append(p[x][ii])
        visited[p[x][ii]] = 1
    while queue:
        hing = queue.pop()
        for aa in p[hing]:  # 부모가 있으면
            if aa not in queue and not visited[aa]:
                queue.append(aa)
                visited[aa] = 1
                if aa not in upper_path:
                    upper_path.append(aa)
    return


def find_child(x):  # 더 작은 애 찾기
    global lower_path
    queue = deque()
    visited = [0] * (N + 1)
    if x in sum(p, []):
        for i in range(1, N+1):
            if x in p[i]:
                for b in p[i]:
                    if b == x:
                        queue.append(i)  # x 보다 작은 것
                        lower_path.append(i)
                        visited[i] = 1
        while queue:
            hing = queue.pop()
            for i in range(1, N + 1):
                for b in p[i]:
                    if b == hing and not visited[i]:
                        queue.append(i)
                        visited[i] = 1
                        if i not in lower_path:
                            lower_path.append(i)
    return

for tc in range(1, int(input()) + 1):
    N = int(input())
    M = int(input())
    p = [[]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        p[a].append(b)
    cnt = 0
    for idx in range(1, N+1):
        upper_path = deque()
        find_parent(idx)
        print(idx, '보다 큰애', upper_path)

        lower_path = deque()
        find_child(idx)
        print(idx, '보다 작은애', lower_path)

        if len(upper_path)+len(lower_path) == N-1:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
