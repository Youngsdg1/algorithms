import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())  # 마지막 노드 번호, 간선의 개수
    arr = [list(map(int, input().split())) for _ in range(E)]   # 노드, 가중치
    print(arr)
