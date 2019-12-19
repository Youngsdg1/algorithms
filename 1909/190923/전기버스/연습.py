def perm(arr, k, x, empty):
    global resl
    if k == m:
        res = []
        for i in range(k):
            res.append(empty[i])
        resl.append(res)
    else:
        for i in range(x, n+1):
            empty.append(i)
            perm(arr, k+1, i, empty)
            empty.pop()

n, m = map(int, input().split())
arr= [0] * n
for i in range(n):
    arr[i] = i+1
res = []
resl = []
perm(arr, 0, 1, [])
print(resl)