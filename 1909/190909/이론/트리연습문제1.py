l = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
Tree = [[0, 0] for _ in range(13)]
for i in range(0, len(l), 2):
    for j in range(13):
        if l[i] == j:
            if not Tree[j][0]:
                Tree[j][0] = l[i+1]
            if Tree[j][0]:
                Tree[j][1] = l[i+1]
print(Tree)
def preorder(T):
    if T:
        print(T)
        try:
            preorder(Tree[T][0])
            preorder(Tree[T][1])
        except IndexError:
            pass
preorder(1)

# teachers
n = int(input())
tree = [[0]*2 for _ in range(n+1)]
templ = list(map(int, input().split()))
for i in range(len(templ)//2):
    parent, child = templ[i*2], templ[i*2+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
def preorder_traverse(T):
    if T:  # 얘네 순서에 따라 Tree 순회 종류가 달라짐
        print('%d' % T, end= '')
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])
preorder_traverse(1)
print()