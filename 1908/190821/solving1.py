import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
    m = int(input())
    square = []
    for _ in range(8):
        s = list(input())
        square.append(s)
    def find(square):
        cnt = 0
        for i in range(8):
            for j in range(8-m+1):
                if square[i][j:j+m] == square[i][j:j+m][::-1]:
                    cnt += 1
                else:
                    pass
        sero = square[:]
        # sero = list(zip(*square))  같은 열에 있는 애들을 모은것
        for i in range(8):
            for j in range(8):
                if i > j:
                    sero[i][j], sero[j][i] = sero[j][i], sero[i][j]
        for i in range(8):
            for j in range(8-m+1):
                if sero[i][j:j+m] == sero[i][j:j+m][::-1]:
                    cnt += 1
                else:
                    pass
        return cnt
    print('#{} {}'.format(tc, find(square)))