import sys
sys.stdin = open('input.txt', 'r')


def perm(company, home, real_chapyo, distance):
    global queue, visited, result
    if n == len(queue):
        distance += (abs(home[0] - queue[-1][0]) + abs(home[1] - queue[-1][1]))
        if result > distance:
            result = distance
    else:
        for i in range(n):
            if visited[i]:
                continue
            else:
                if not queue:  # 첫번째 애일때는 값을 그냥 추가
                    new = abs(company[0] - real_chapyo[i][0]) + abs(company[1] - real_chapyo[i][1])
                else:  # 두번째부터는 값 입력 후 븨즤틔드
                    new = abs(real_chapyo[i][0] - queue[-1][0]) + abs(real_chapyo[i][1] - queue[-1][1])
            visited[i] = 1
            queue.append(real_chapyo[i])
            distance += new
            if distance <= result:
                perm(company, home, real_chapyo, distance)
            distance -= new
            visited[i] = 0
            queue.pop()


for tc in range(1, int(input()) + 1):
    n = int(input())
    chapyo = list(map(int, input().split()))
    company = [0, 0]
    company[0], company[1] = chapyo[0], chapyo[1]
    home = [0, 0]
    home[0], home[1] = chapyo[2], chapyo[3]
    result = 10000
    real_chapyo = []
    for i in range(0, n * 2, 2):
        real_chapyo.append(chapyo[4 + i:6 + i])
    print(real_chapyo)
    visited = [0] * n
    queue = []
    distance = 0
    perm(company, home, real_chapyo, distance)
    print('#{} {}'.format(tc, result))