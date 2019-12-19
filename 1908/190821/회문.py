import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())  # n * n 행렬, m은 찾을 패턴의 길이
    arr = []
    for _ in range(n):
        arr.append(list(input()))

    def my_find():
        for i in range(n):
            for j in range(n//2):
                if arr[i][j:j+m+1] == arr[i][j:j+m+1][::-1]:  # 가로 회문 찾는거
                    return ''.join(arr[i][j:j+m+1])
                    break
                else:
                    pass
        sero = arr[:]
        for i in range(n):
            for j in range(n):
                if i > j:
                    sero[i][j], sero[j][i] = sero[j][i], sero[i][j]
        for i in range(n):
            for j in range(n//2):
                if sero[i][j:j+m+1] == sero[i][j:j+m+1][::-1]:  # 가로 회문 찾는거
                    return ''.join(sero[i][j:j+m+1])
                    break
                else:
                    pass
    print('#{} {}'.format(tc, my_find()))

    # 세로 배열 리스트 만들기
    # col = [[0] * n for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         col[i][j] = arr[j][i]
    # print(col)
