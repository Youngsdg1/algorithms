N, M = map(int, input().split())
t1 = [0]*N
result = []
l = [n for n in range(1, N+1)]
def perm(k):
    global M, N
    t = t1
    if k == M:
        print(t)
    else:
        for i in range(N):
            if k == 0:
                t[k] = l[i]
                perm(k + 1)
            else:
                if l[i] >= t[k-1]:
                    t[k] = l[i]
                    perm(k+1)
perm(0)