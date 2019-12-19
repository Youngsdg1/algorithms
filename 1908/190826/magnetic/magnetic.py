import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
        V = int(input())
        arr = [[0] * 101 for _ in range(101)]
        for i in range(100):
            arr[i] = (list(map(int, input().split())))
        # arr = [input().split() for _ in range(N)]
        cnt = 0
        for i in range(100):
            for j in range(100):  # 한 행씩 보는거임
                # N극에서 시작할 때 (위)
                if arr[i][j] == 1:
                    # 한 칸씩 내려
                    if arr[i+1][j] == 2:  # 2가 나오면 cnt
                        cnt += 1
                    elif arr[i+1][j] == 0:  # 0이면 이동
                        arr[i+1][j] = arr[i][j]
                # # S극에서 시작할 때 (아래)
                # if arr[100-i-1][j] == 2:
                #     #한 칸씩 올라가면서
                #     if arr[i+1][j] == 1:  # 1이 나오면 cnt
                #         cnt += 1
                #     elif arr[i+1][j] == 0:
                #         arr[i+1][j] = arr[i][j]
                #     elif arr[i+1][j] == 2:
                #         pass
        print('#{} {}'.format(tc, cnt))