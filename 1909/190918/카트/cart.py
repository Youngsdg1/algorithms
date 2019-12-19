import sys
sys.stdin = open('input.txt', 'r')
def dfs(path):
    global min
    a = path[-1]
    if a < n:
        visited = [0] * n
        res = 0
        res += arr[0][path[-1]]
        visited[path[-1]] = 1
        for i in range(n):
            if visited[i]:
                continue
            elif visited[i] == 0 and arr[path[-1]][i] != 0:
                visited[i] = 1
                res += arr[path[-1]][i]
                path.append(i)
                if sum(visited) == n:
                    res += arr[path[-1]][0]
                    if min > res:
                        min = res
                elif arr[path[-1]][i] == 0:
                    path.remove(i)
        dfs([a + 1])
    else:
        return

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    min = 99999
    dfs([1])

    print('#{} {}'.format(tc, min))