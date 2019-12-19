import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    sadari = []
    for i in range(100):
        sadari.append(list(map(int, input().split())))