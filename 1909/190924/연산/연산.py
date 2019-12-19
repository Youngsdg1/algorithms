import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
def bfs(v):
    queue = deque([v])
    visited = [0] * 1000001
    visited[v] = 1
    while queue:
        s = queue.popleft()
        if s == M:
            return visited[s]-1
        else:
            if s + 1 <= 1000000:
                if visited[s + 1] == 0:
                    queue.append(s + 1)
                    visited[s + 1] = visited[s] + 1
            if s - 1 > 1:
                if visited[s - 1] == 0:
                    queue.append(s - 1)
                    visited[s - 1] = visited[s] + 1
            if s * 2 <= 1000000:
                if visited[s * 2] == 0:
                    queue.append(s * 2)
                    visited[s * 2] = visited[s] + 1
            if s - 10 > 1:
                if visited[s - 10] == 0:
                    queue.append(s - 10)
                    visited[s - 10] = visited[s] + 1
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # 연산 전 자연수, 연산 후 자연수
    print('#{} {}'.format(tc, bfs(N)))