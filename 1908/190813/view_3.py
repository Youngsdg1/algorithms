for tc in range(1, 11):
    num = int(input())
    b = list(map(int.input().split()))
    result = 0
    for n in range(2, num-1):
        if max(b[n-2:n+3]) == b[n]: #내 자신이 제일 큰 경우
            result += b[n] - sorted(b[n-2:n+3])[3]
    print()