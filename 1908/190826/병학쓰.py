import sys
sys.stdin = open('input.txt','r')
a = int(input())
def find(miro):
    for p in range(len(miro)):
        for q in range(len(miro)):
            if miro[p][q] == 2:
                return navi(miro,p,q)
def navi(miro, p, q):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    x, y = p, q
    stack = []
    visited = []
    stack.append((x, y))
    while stack:
        x=stack[-1][0]
        y = stack[-1][1]
        for i in range(4):
            if 0<= x+dx[i] <=len(miro)-1 and 0<= y+dy[i] <= len(miro)-1:
                if miro[x+dx[i]][y+dy[i]] == 3:
                    return 1
                if miro[x+dx[i]][y+dy[i]] == 0 and (x+dx[i], y+dy[i]) not in visited:
                    x = x+dx[i]
                    y = y+dy[i]
                    stack.append((x,y))
                    visited.append((x,y))
                    break
        else:
            stack.pop()
    return 0
for n in range(a):
    b = int(input())
    miro = [list(map(int,input())) for _ in range(b)]
    result = find(miro)
    print('#{} {}'.format(n+1, result))