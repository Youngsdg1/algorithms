l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l)
col = [[0] * 3] * 3
print(col)
for i in range(3):
    for j in range(3):
        col[i][j] = l[i][j]
print(col)

# 빈 3*3 찐행렬 만들려면 이렇게 해야됨!!!
col = [[0]*3 for _ in range(3)]