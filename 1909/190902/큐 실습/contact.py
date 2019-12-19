import sys
sys.stdin = open("contact.txt", "r")
for tc in range(1, 11):
    n, start = map(int, input().split())
    input_list = list(map(int, input().split()))
    nodelist = [[] for _ in range(1, n+1)]
    for i in range(0, n, 2):
        nodelist[input_list[i]].append(input_list[i+1])

    def bfs(nodelist, x):
        visited = [0] * (max(sum(nodelist, []))+1)
        queue = [x]  # 시작점은 x
        a = 1
        while queue:  # queue 가 빌 때 까지 탐색을 계속
            vertex = queue.pop(0)  # 선입선출/ 큐의 맨 앞 원소를 방문할 지점으로 설정
            if visited[vertex] == 0:
                visited[vertex] = a
                if nodelist[vertex] != []:  # x의 인접 정점이 있으면
                    a += 1
                    for i in nodelist[vertex]:  # 걔네 중
                        if visited[i] == 0:  # 방문 안한 정점이 있으면
                            queue.append(i)  # 큐 에 추가
        print(visited)
        for i in range(max(sum(nodelist, [])), 0, -1):
            if visited[i] == max(visited):
                return i

    print(bfs(nodelist, 2))