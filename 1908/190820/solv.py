import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
    T = int(input())
    arr = []  # 엣지문제 방지를 위해 맨 위에 0으로 된 줄 추가
    arr = []
    for i in range(100):
        arr.append([0] + list(map(int, input().split())) + [0])  # 엣지문제 방지를 위해 양옆 0으로 된 줄 추가
    for i in range(1,101):  # 2인 부분에서 시작
        if arr[99][i] == 2:  # 양 옆줄 이랑 맨 위에 한 줄 추가한 것을 고려
            x = 99
            y = i
            break
    a = x
    b = y
    while a != 0:
        if arr[a][b-1] == 0 and arr[a][b+1] == 1:  # 오른쪽으로 가는 경우
                while arr[a][b+1] == 1:
                    arr[a][b] = 0
                    b = b + 1
        elif arr[a][b+1] == 0 and arr[a][b-1] == 1:  # 왼쪽으로 가는 경우
                while arr[a][b-1] == 1:
                    arr[a][b] = 0
                    b = b - 1
        else:
            arr[a][b] = 0
        a -= 1
    print('#{} {}'.format(T, b - 1))