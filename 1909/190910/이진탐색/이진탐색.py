import sys
sys.stdin = open('input.txt', 'r')
def func(t):
    global count
    if arr[t]:
        func(2*t)
        count += 1
        temp = count
        tree[t] = temp
        func(2*t+1)
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [i for i in range(N+1)] + [0]*(N+1)
    tree = [0] * (N+1)
    count = 0
    func(1)
    print('#%d %d %d' % (tc, tree[1], tree[N//2]))