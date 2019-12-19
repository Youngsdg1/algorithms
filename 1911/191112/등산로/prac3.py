# N 까지 자연수 중에서 M 개를 고른 수열
t = [0] * 6
l = [n for n in range(1, 6+1)]
def p(n, k):
    global t
    if k == n:
        print(t)
    else:
        for i in range(n):
            if k == 0:
                t[k] = l[i]
                p(n, k+1)
            else:
                if l[i] >= t[k-1]:
                    t[k] = l[i]
                    p(n, k+1)
p(6, 0)