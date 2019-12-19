import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    m = int(input())
    n = list(map(int, input().split()))

    for i in range(n):
        found = False
        if arr[ i * 2] == arr[j * 2 + 1] :
            found = True
            break
        if found == False:
            start_position = i
            break