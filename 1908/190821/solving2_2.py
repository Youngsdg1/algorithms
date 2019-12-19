import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
    T = int(input())
    square = [[0] * 100 for i in range(100)]
    for i in range(100):
        square[i] = list(input())

    def find(square):
        l_r = []
        for i in range(100):
            for j in range(100):
                for m in range(0, len(square[i]) - j + 1):
                    if square[i][j:j + m] == square[i][j:j + m][::-1]:
                        if m > 9:
                            l_r.append(m)
        #print(1, l_r)
        sero = square
        for i in range(100):
            for j in range(100):
                if i > j:
                    sero[i][j], sero[j][i] = sero[j][i], sero[i][j]
        l_c = []
        for i in range(100):
            for j in range(100):
                for m in range(0, len(square[i]) - j + 1):
                    if sero[j:j + m][i] == sero[j:j + m][i][::-1]:
                        if m > 9:
                            l_c.append(m)
        #print(2, l_c)
        a = max(l_r)
        b = max(l_c)
        #print(a, b)
        if a > b:
            return a
        else:
            return b
    print('#{} {}'.format(tc, find(square)))  # 7, 5, 1번 오답