# 원소의 합이 10인 부분집합 구하기
ipt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = [0] * 10
visited = [0] * 10
n = len(ipt)
def perm(k):
    if k == n:
        print(t)
    else:
        for i in range(10):
            if visited[i] == 0:
                visited[i] = 1
                t[k] = ipt[i]
                perm(k+1)
                visited[i] = 0

def powerset(k):
    if k == n:
        if sum(t) == 10:
            for i in t:
                if i != 0:
                    print(i, end=' ')
            print()
    else:
        t[k] = ipt[k]
        powerset(k+1)
        t[k] = 0
        powerset(k+1)

powerset(0)