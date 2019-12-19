
def calc(li):
    l = li[:]
    for c in range(1, len(l), 2):
        if l[c] == '+':
            l[c+1] = l[c-1]+l[c+1]
        elif l[c] == '-':
            l[c+1] = (l[c-1] - l[c+1])
        else:
            l[c+1] = (l[c-1] * l[c+1])
    return l[-1]

def group(k, N):
    global max_v
    t = cal[:]
    if k == N:
        for ii in range(len(l2)):
            if t[l2[ii]] == '+':
                t[l2[ii]-1] += t[l2[ii]+1]
            elif t[l2[ii]] == '-':
                t[l2[ii] - 1] -= t[l2[ii] + 1]
            elif t[l2[ii]] == '*':
                t[l2[ii] - 1] *= t[l2[ii] + 1]
        if l2:
            for ii in range(len(l2)-1, -1, -1):
                t.pop(l2[ii])
                t.pop(l2[ii])
        re = calc(t)
        if re > max_v:
            max_v = re
    else:
        for ii in range(len(l)):
            if visited[ii]:
                continue
            if l2:
                if abs(l.index(l2[-1])-ii) != 1 and l2[-1] < l[ii]:
                    l2.append(l[ii])
                    visited[ii] = 1
                    group(k+1, N)
                    visited[ii] = 0
                    l2.pop()
            else:
                l2.append(l[ii])
                visited[ii] = 1
                group(k + 1, N)
                visited[ii] = 0
                l2.pop()
import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
inp = input()
cal = [0]*N
l = [i for i in range(1, N, 2)]
l2 = []
max_v = -(2**31)
visited = [0]*N
for idx in range(N):
    if inp[idx] == '-':
        cal[idx] = '-'
    elif inp[idx] == '+':
        cal[idx] = '+'
    elif inp[idx] == '*':
        cal[idx] = '*'
    else:
        cal[idx] = int(inp[idx])
for s in range(len(l)//2+1):
    group(0, s)
print(max_v)