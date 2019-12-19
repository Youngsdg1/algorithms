# 181, 197쪽
v_list = list(map(int, input().split(',')))
# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7

arr = []
for i in range(8):
    arr.append([0] * 8)  # 7 * 7 행렬

for i in range(0, len(v_list), 2):
    arr[v_list[i]][v_list[i+1]] = 1
    arr[v_list[i+1]][v_list[i]] = 1

visited = [0] * 8
stack = []
top = -1


def DFS(v):
    visited[v+1] = 1
    stack.append(v)
    while stack:
        stack.pop()
        v = stack[-1]  # 전걸로 돌아간거야, 그래서 이제 시작점이 w가 된거야
        return w
        while w:
            for i in range(1, 8):
                if arr[v][i] == True and visited[i + 1] == 0:  # 인접행렬 중 방문하지 않은 애 찾기, v가 출발지, i가 도착지
                    w = arr[v][i]  # 이제 도착지가 출발지가 됨
                    visited[w + 1] = 1
                    stack.append(w)
def findnext():
    for i in range(1, 8):
        if arr[v][i] == True and visited[i + 1] == 0:  # 인접행렬 중 방문하지 않은 애
            return i
        else:
            return 0

print(DFS(1))