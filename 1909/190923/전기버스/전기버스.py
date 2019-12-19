import sys
sys.stdin = open('input.txt', 'r')
def move(steps, n):
    global min_ch
    if steps >= N - 1:
        if n < min_ch:
            min_ch = n
    else:
        for step in range(1, 1 + li[steps]):  # 이동시킨거
            if n + 1 < min_ch:
                move(steps + step, n + 1)
for tc in range(1, int(input())+1):
    li = list(map(int, input().split()))
    print(li)
    li.append(0)
    N = li.pop(0)
    min_ch = 100
    move(0, 0)
    print('#%d %d' % (tc, min_ch-1))