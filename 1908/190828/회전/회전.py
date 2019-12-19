import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    Q = l + [0] * 1000
    front = -1
    rear = n - 1
    t = 0
    while t < m+1:
        front += 1
        rear += 1
        Q[rear] = Q[front]
        t += 1
    print('#{} {}'.format(tc, Q[m+n]))
