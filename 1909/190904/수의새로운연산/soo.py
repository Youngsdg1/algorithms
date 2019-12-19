def sooro(x, y):  # 가로 시작값 구하고, 세로로 더하기
    ans = 1
    a = x
    for i in range(2, x + 1):
        ans += i
    for j in range(y - 1):
        ans += a
        a += 1
    return ans

def chapyoro(z):
    k = 1
    g = 0
    while g != z:
        f = 0
        for r in range(k):
            g += 1
            f += 1
            if g == z:
                break
        k += 1
    return [f, k - f]

import sys
sys.stdin = open('soo.txt', 'r')
for tc in range(1, int(input())+1):
    p, q = map(int, input().split())
    print('#{} {}'.format(tc, sooro(chapyoro(p)[0]+chapyoro(q)[0], chapyoro(p)[1]+chapyoro(q)[1])))