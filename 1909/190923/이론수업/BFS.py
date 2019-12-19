tin = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
edges = [[] for i in range(8)]
while tin:  # 쌍방향 정점 만들기
    x = tin.pop()
    y = tin.pop()
    edges[x].append(y)
    edges[y].append(x)
visited = [0] * 8
def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        for u in edges[s]:
            if visited[u] == 0:
                queue.append(u)
                visited[u] = 1
bfs(1)