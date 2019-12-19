import sys
sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
virus = []
visited = [[0] * N for _ in range(N)]

def bfs(A):
    pass

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            bfs([i. j])
# 0 은 빈칸, 1은 벽, 2는 바이러스
# bfs로 탐색하면서 visited에 1씩 증가시켜줌

# for 문 돌다가 2가 있으면 bfs
# 인접한 모든 빈칸 보게 돌리고 갯수가 M 되면 return
# visited가 변화가 없으면 -1 출력

