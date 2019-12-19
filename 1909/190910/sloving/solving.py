# 후위로 돌면서 연산 처리
import sys
sys.stdin = open('input.txt', 'r')

def func(node):
    lc, rc = tree[node][0], tree[node][1]
    if node:
        func(lc)
        func(rc)
        if values[node] == '+':
            values[node] = values[lc] + values[rc]
        elif values[node] == '-':
            values[node] = values[lc] - values[rc]
        elif values[node] == '/':
            values[node] = values[lc] / values[rc]
        elif values[node] == '*':
            values[node] = values[lc] * values[rc]

for tc in range(1, int(input())+1):
    n = int(input())
    data = [list(input().split()) for _ in range(n)]
    tree = [[0]*2 for _ in range(n+1)]
    values = [0] * (n+1)
    print('data', data)
    for i in data:
        if len(i) > 3:
            node, val, lc, rc = int(i[0]), 1, 2, 3
            values[node] = val
            tree[node][0] , tree[node][1] = lc, rc
        else:
            i[0], i[1] = lc, rc
    print('tree', tree)
