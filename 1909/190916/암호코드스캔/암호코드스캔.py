import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    print(arr)