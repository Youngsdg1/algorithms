# 완전이진트리
# 후위순회하면서 값 더해주기
import sys
sys.stdin = open('input.txt', 'r')

def func(T):
    if 2 * T < N:
        tree[T] = func(T * 2) + func(T * 2 + 1)
        return tree[T]
    elif 2 * T == N:
        tree[T] = tree[2 * T]
        return tree[2 * T]
    else:
        return tree[T]

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    leaf_node_list = [list(map(int, input().split())) for _ in range(M)]
    tree = [0] * (N + 2)
    node_list = []
    for i in leaf_node_list:
        tree[i[0]] = i[1]
        node_list.append(i[0])
    func(1)
    print('#{} {}'.format(tc, tree[L]))

