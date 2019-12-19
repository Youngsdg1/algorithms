g = 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 3, 7, 6, 7
arr = [[0] * 8 for _ in range(8)]

for j in range(0, 16, 2):
    arr[g[j]][g[j+1]] = 1
    arr[g[j + 1]][g[j]] = 1
G = arr
result = []

def BFS(G, v):  # 그래프 G, 탐색 시작점 v
    visited = [0] * 8  # n 정점의 개수
    queue = []
    queue.append(v)  # 시작점 v를 큐에 삽입
    while queue:  # 큐가 비어있지 않은 경우
        t = queue.pop()  # 큐의 첫번째 원소 반환
        if not visited[t]:  # 방문되지 않은 곳이라면
            visited[t] = True  # 방문한 것으로 표시
            result.append(t)
        for i in range(len(G[t])):  # t와 연결된 모든 선에 대해
            if G[t][i] == 1 and visited[i] == 0:  # 방문되지 않은 곳이라면
                queue.append(i)  # 큐에 넣기
    return ' '.join(map(str, result))

print(BFS(G, 1))