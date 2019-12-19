for tc in range(1, 4):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    x, y = 0, 0
    dx, dy = 0, 1
    cnt = 0
    while 0 <= x + dx < n and 0 <= y + dy < n:
        x += dx
        y += dy
        if arr[x][y] == 1:
            dx, dy = -dy, -dx
        if arr[x][y] == 2:
            dx, dy = dy, dx
        cnt += 1

    print('#%d %d' % (tc, cnt))