import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    Ci = list(map(int, input().split()))

    pizza_index = []
    for i in range(m):
        pizza_index.append([Ci[i], (i+1)])

    fire = []
    for i in range(n):
        a = pizza_index.pop(0)
        fire.append(a)
    count = 0
    last_pizza = 0
    def pizza(fire, n):
        global last_pizza, count
        while fire:
            a = fire.pop(0)
            if count >= n:
                a[0] = a[0] // 2
                last_pizza = a[1]
            if a[0] == 0:
                if pizza_index:
                    fire.append(pizza_index.pop(0))
                else:
                    fire.append([0, 0])
            else:
                fire.append(a)
            count += 1
            cnt = 0
            for i in range(n):
                if fire[i][0] == 0:
                    cnt += 1
            if cnt == n:
                break

    pizza(fire, n)
    print('#{} {}'.format(tc, last_pizza))
