import sys
sys.stdin = open('input.txt', 'r')
def func(t):
    global cnt
    if tree == empty_tree:
        tree[1] = t
    else:
        temp = cnt+1
        tree[temp] = t
        temp_temp = temp//2
        while temp_temp >= 0:
            if tree[temp] < tree[temp_temp]:
                tree[temp_temp], tree[temp] = tree[temp], tree[temp_temp]
                temp = temp // 2
                temp_temp = temp_temp//2
            else:
                break
        cnt += 1
for tc in range(1, int(input())+1):
    N = int(input())
    unsorted = list(map(int, input().split()))
    tree = [0] * (N+1)
    empty_tree = [0] * (N + 1)
    cnt = 1
    sum_node = 0
    for i in unsorted:
        func(i)
    index = N
    print(tree)
    while index > 0:
        sum_node += tree[index//2]
        index = index//2
    print('#{} {}'.format(tc, sum_node))