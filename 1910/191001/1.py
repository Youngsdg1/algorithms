# 과제 2번
tree =[]
def find_child(root):
    print(root, end=' ')
    if tree[root]:
        for i in range(len(tree[root])):
            if i == 0:
                print('--+- {}'.format(tree[root][i]))
                find_child(tree[root][i])
            if i == len(tree[root] - 1):
                print('L--- {}'.format(tree[root][i]))
                find_child(tree[root][i])
            else:
                print('+--- {}'.format(tree[root][i]))
                find_child(tree[root][i])

# 과제 3번
# 제일 먼저 곱해야하는 두 개의 행렬 찾기
N_list = [[1, 2], [2, 1]]
result = []

def sequence(N_list, n):
    global result
    if n > 1:
        min_h = 9999
        min_y = 9999
        min_n = 9999
        n = 2
        for i in range(n):
            if min_h > N_list[i][0]:  # 이때의 시작점은 min_h
                min_h = N_list[i][0]  # 가장 작은 행 과 그때의 가장 작은 열 찾기
                if min_y > N_list[i][1]:  # 이때의 끝점은 min_y
                    min_y = N_list[i][1]
        for i in range(n):
            if N_list[i][0] == min_y:  # 위의 경우에 곱해지는 행렬 찾기, 이때의 시작점은 min_y
                if min_n > N_list[i][1]:
                    min_n = N_list[i][1]  # 이때의 끝점은 min_n
        result.append([min_h, min_y])
        result.append([min_y, min_n])
        N_list.remove([min_h, min_y])
        N_list.remove([min_y, min_n])
        N_list.append([min_h, min_n])
        sequence(N_list, n-1)

sequence(N_list, 2)
print(result)
