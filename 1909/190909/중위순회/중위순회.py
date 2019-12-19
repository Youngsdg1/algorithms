import sys
sys.stdin = open('input.txt', 'r')
def preorder_traverse(T):
    if T:
        preorder_traverse(tree[T][0])
        print('%s' % alpha[T], end='')
        preorder_traverse(tree[T][1])
for tc in range(1, int(input())+1):
    n = int(input())
    alpha = [0] * (n+1)
    tree = [[0] * 2 for _ in range(n + 1)]
    for _ in range(n):
        templ = list(input().split())
        alpha[_ + 1] = templ[1]
        for i in range(2, 4):
            try:
                if templ[2]:
                    parent, child = int(templ[0]), int(templ[2])
                    tree[int(templ[0])][0] = int(templ[2])
                if templ[3]:
                    parent, child = int(templ[0]), int(templ[3])
                    tree[int(templ[0])][1] = int(templ[3])
            except IndexError:
                pass
    print('#{}'.format(tc), end=' ')
    preorder_traverse(1)
    print()