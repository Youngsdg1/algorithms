import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
    T = int(input())
    arr = [[0] * 100]  # 엣지문제 방지를 위해 맨 위에 0으로 된 줄 추가
    for i in range(100):
        arr.append([0] + list(map(int, input().split())) + [0])  # 엣지문제 방지를 위해 양옆 0으로 된 줄 추가

    def sadari(a, b):  # location = (a, b) = (행, 열)
        if arr[a-1][b] == 1:  # 위로 올라감
            a = a - 1
            b = b
            if arr[a][b-1] == 0 and arr[a][b+1] == 1:  # 오른쪽으로 가는 경우
                while arr[a][b] != 0:
                    a = a
                    b = b + 1
                return sadari(a, b)
            elif arr[a][b+1] == 0 and arr[a][b-1] == 1:  # 왼쪽으로 가는 경우
                while arr[a][b] != 0:
                    a = a
                    b = b - 1
                return sadari(a, b)

            elif arr[a][b + 1] == 0 and arr[a][b - 1] == 0:  # 위로 가는 경우
                return sadari(a, b)
        else:
            if arr[a][b+1] == 0 and arr[a][b-1] == 1:  # 왼쪽으로 가는 경우
                while arr[a][b] != 0:
                    a = a
                    b = b - 1
                return sadari(a, b)

            elif arr[a][b + 1] == 0 and arr[a][b - 1] == 0:  # 위로 가는 경우
                return sadari(a, b)

    for i in range(100):  # 2인 부분에서 시작
        if arr[100][i - 1] == 2:  # 양 옆줄 이랑 맨 위에 한 줄 추가한 것을 고려
            x = 100
            y = i - 1

    print(x, y)
    print(sadari(x, y))
