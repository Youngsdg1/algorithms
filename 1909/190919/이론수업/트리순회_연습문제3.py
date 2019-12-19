n = 12
l = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
Tree = [[] for _ in range(13)]
for i in range(0, len(l), 2):
    Tree[l[i]].append(l[i+1])
    # 무조건 2개니까 Tree[l[i]][0] != 0 일때 여기에 값 추가 이런식으루
print(Tree)

def preorder(T):
    if T:  # if node != none 이라는 뜻
        print(T)
        try:
            preorder(Tree[T][0])
            preorder(Tree[T][1])
        except IndexError:
            pass
preorder(1)
print()
def inorder(T):
    if T:
        try:
            preorder(Tree[T][0])
            print(T)
            preorder(Tree[T][1])
        except IndexError:
            pass
inorder(1)
print()
def postorder(T):
    if T:
        try:
            preorder(Tree[T][0])
            preorder(Tree[T][1])
            print(T)
        except IndexError:
            pass
postorder(1)
