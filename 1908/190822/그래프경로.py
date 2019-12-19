import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())  # E개
    arr = [[0]*(v+1) for _ in range(v+1)]  # v*v 행렬
    for _ in range(e):
        dep, arrive = map(int, input().split())
        arr[dep][arrive] = 1  # 인접행렬
    s, g = map(int, input().split())  # 출발, 도착 노드
    print(s, g)
    def findnext(s, stack):
        for i in range(1, v+1):
            if arr[s][i] == 1 and visited[i] == 0:
                return i
        else:
            stack.pop()
            return stack[-1]
    # 들어오는 간선의 개수를 count를 해주면서 0이될때 가게 한다.
    # DFS - s 에서 출발했을때 g까지 갈 수 있는가
    visited = [0] * (v+1)
    stack = [0, s]
    def DFS(s):
        visited[s] = 1
        while len(stack) != 1:
            f = findnext(s, stack)
            s = f
            if visited[f] == 0:
                visited[f] = 1
                stack.append(f)
        if visited[g] == 1:
            print('#{} {}'.format(tc, 1))
        else:
            print('#{} {}'.format(tc, 0))
    DFS(s)