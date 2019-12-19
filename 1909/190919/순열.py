
# 0부터 n까지의 수 순열 구하기

# a = [0, 1, 2]
# def perm(arr, empty, k, visited):
#     if len(arr) == len(empty):
#         print(empty)
#     else:
#         for i in range(len(arr)):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 empty.append(arr[i])
#                 perm(arr, empty, k+1, visited)
#                 empty.pop()
#                 visited[i] = 0
# perm(a, [],0,  [0]*len(a))

a = [0, 1, 2]
n = len(a)
def perm(arr, empty, k, visited):
    if k == n:
        print(empty)
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                empty.append(arr[i])
                perm(arr, empty, k+1, visited)
                empty.pop()
                visited[i] = 0
perm(a, [], 0, [0]*n)
