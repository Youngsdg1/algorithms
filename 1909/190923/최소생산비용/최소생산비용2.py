import sys
sys.stdin = open('input.txt', 'r')
def perm(arr, visited, empty, k):
    global min_value
    if k == N:
        sum_fact = 0
        for i in range(N):
            sum_fact += arr[i][empty[i]]
        if sum_fact < min_value:
            min_value = sum_fact
    else:
        for i in range(N):
            if visited[i] == 0:
                empty.append(i)
                visited[i] = 1
                sum_fact = 0
                for j in range(len(empty)):
                    sum_fact += arr[j][empty[j]]
                if sum_fact < min_value:
                    perm(arr, visited, empty, k + 1)
                visited[i] = 0
                empty.pop()
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_value = 99999999
    perm(arr, [0]*N, [], 0)
    print('#{} {}'.format(tc, min_value))