import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    v, e = map(int, input().split())  # 노드 개수, 간선 개수
    node_list = [list(map(int, input().split())) for _ in range(e)]  # 간선 노드 번호
    s, g = map(int, input().split())  # 출발노드, 도착노드
    visited = []
    start = s
    cnt = 0
    def bfs(start):
        global cnt
        queue = [start]
        visited.append(start)
        while queue:
            cnt += 1
            for _ in range(len(queue)):
                a = queue.pop(0)
                for i in node_list:
                    if i[0] == a:
                        if i[1] not in visited:
                            visited.append(i[1])
                            queue.append(i[1])
                            if i[1] == g:
                                return cnt
                    elif i[1] == a:
                        if i[0] not in visited:
                            visited.append(i[0])
                            queue.append(i[0])
                            if i[0] == g:
                                return cnt
        cnt = 0
        if cnt == 0:
            return 0
    print('#{} {}'.format(tc, bfs(s)))

