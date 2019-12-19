import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    n = int(input()) // 10
    def jague(n):
        if n == 1:
            return n
        if n == 2:
            return 3
        return jague(n-1) + (2*jague(n-2))
    print('#{} {}'.format(tc, jague(n)))

