# inorder든 preorder든 하면서 count 해주면됨
import sys
sys.stdin = open('input.txt', 'r')
def preorder_traverse(T):
    global cnt
    if T:
        preorder_traverse(tree[T][0])
        cnt += 1
        preorder_traverse(tree[T][1])

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())  # 간선의 개수
    templ = list(map(int, input().split()))  # 부모 자식 노드 쌍
    tree = [[0] * 2 for _ in range(E+2)]
    for i in range(len(templ) // 2):
        parent, child = templ[i * 2], templ[i * 2 + 1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
    cnt = 0
    preorder_traverse(N)
    print('#{} {}'.format(tc, cnt))