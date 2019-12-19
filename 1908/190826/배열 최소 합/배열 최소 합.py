import sys
sys.stdin = open('by.txt','r')

def perm(arr, visited, empty, k):
    global min_val, res
    if k == N:
        fun_sum = 0
        for i in range(N):
            fun_sum += arr[i][empty[i]]
        if min_val > fun_sum:
            min_val = fun_sum
    else:
        for j in range(N):
            if visited[j] == 0:
                empty.append(j)
                visited[j] = 1
                fun_sum = 0
                for i in range(len(empty)):
                    fun_sum += arr[i][empty[i]]
                if min_val > fun_sum:
                    perm(arr, visited, empty, k + 1)
                empty.pop()
                visited[j] = 0
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_val = 999999
    res = []
    perm(arr, [0]*N, [], 0)
    print('#{} {}'.format(tc,min_val))