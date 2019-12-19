li = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
arr = [[]  for _ in range(len(set(li))+1)]
for i in range(0, len(li), 2):
    arr[li[i]].append(li[i+1])
visited = [0] * (len(set(li))+1)
def dfs_Recursive(v):
    visited[v] = 1
    print(v, end=' ')
    for i in arr[v]:
        if visited[i] == 0:
            dfs_Recursive(i)
dfs_Recursive(1)

def dfs(v, arr):
    stack = []
    stack.append(v)
    while stack:
        v = stack.pop(-1)
        if visited[v] == 0:
            visited[v] = 1
            print(v, end=' ')
            for w in arr[v]:
                if visited[w] == 0:
                    stack.append(w)
dfs(1, arr)


tin = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
edges = [[] for i in range(8)]
while tin:  # 쌍방향 정점 만들기
    x = tin.pop()
    y = tin.pop()
    edges[x].append(y)
    edges[y].append(x)
visited = [0] * 8

def dfsr_teachers(v):
    visited[v] = 1
    print(v, end=' ')
    for w in edges[v]:
        if not visited[w]:
            dfsr_teachers(w)

def dfs_teachers(v):
    s = []
    s.append(v)
    while s:
        v = s.pop(-1)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in edges[v]:
                if not visited[w]:
                    s.append(w)