# 부분집합 합 문제
# an 모든 부분집합 중 원소의 합이 0이 되는 부분집합 출력하기

# 조합으로 풀기
# def comb(n, r):
#     if r == 0:  # 다 만들어진 경우
#         if sum(tr) == 0:
#             print(tr)
#     elif n < r:  # r의 값이 줄지 않는 경우
#         return
#     else:
#         tr[r-1] = an[n-1]
#         comb(n-1, r-1)
#         comb(n-1, r)
# an = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# n = len(an)
# for i in range(1, n):
#     tr = [0] * i
#     comb(n, i)
#
# # 부분집합으로 풀기
# for i in range(0, (1<<n)):  # 1 << n 은 부분집합의 개수. 2^n
#     result = []
#     for j in range(0, n):  # 원소의 수만큼 비트를 비교함
#         if i & (1<<j):
#             result.append(an[j])
#             if sum(result) == 0:
#                 print(result)
#
# import itertools
# setList = []
# for i in range(1, n+1):
#     subset = list(itertools.combinations(an, i))
#     for j in range(len(subset)):
#         sum = 0
#         subset[j] = list(subset[j])
#     for k in range(len(subset[j])):
#         sum += subset[j][k]
#     if sum == 0:
#         print(subset[j])

def power_set(k, n, t, arr):
    if k == n:
        print(t)
    else:
        t[k] = arr[k]
        power_set(k+1, n, t, arr)
        t[k] = 0
        power_set(k + 1, n, t, arr)

power_set(0, 4, [0] * 4, [1, 2, 3, 4])

def perm(arr, k, empty, visited):
    if k == m:
        print(' '.join(map(str, empty)))
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                empty.append(arr[i])
                perm(arr, k+1, empty, visited)
                empty.pop()
                visited[i] = 0

n, m = map(int, input().split())
arr= [0] * n
for i in range(n):
    arr[i] = i+1
perm(arr, 0, [], [0]*n)