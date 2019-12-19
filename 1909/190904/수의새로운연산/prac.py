def sooro(x, y):
    global ans
    ans = 1
    a = x
    for i in range(2, x + 1):
        ans += i
    for j in range(y-1):
        ans += a
        a += 1
    return ans