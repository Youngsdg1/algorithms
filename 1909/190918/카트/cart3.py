import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 0 부터 n 까지의 순열을 만들고, 인덱스를 붙여서 2개씩 보기
    semi_res = []
    min_sum = 100000
    def perm(a, empty, visitied, k, arr):
        global min_sum
        flag = True
        if k == n:
            if empty[-1] == 0:
                print('ㅇㅇ', empty)
                s = 0
                for i in range(n):
                    if empty[i] == i:
                        flag = False
                        break
                if flag:
                    for i in range(n):
                        s += arr[i][empty[i]]
                        print('수', tc, arr[i][empty[i]])
                    if min_sum > s:
                        min_sum = s
        else:
            for i in range(n):
                if visitied[i] == 0:
                    visitied[i] = 1
                    empty.append(a[i])
                    perm(a, empty, visitied, k+1, arr)
                    empty.pop()
                    visitied[i] = 0
    a = [_ for _ in range(n)]
    perm(a, [], [0] * n, 0, arr)
    print(min_sum)

