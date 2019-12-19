import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    res = []
    for i in range(5):
        res.append(a[-i - 1])
        res.append(a[i])

    print('#{} {}'.format(tc, ' '.join(map(str, res))))
