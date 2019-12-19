def find_chage(battery, now_bat, change, cur):
    global min_value
    if cur == len(battery):
        if min_value > change:
            min_value = change
    else:
        if now_bat > 0:   # 교체 안하고 최대한 가보기
            find_chage(battery, now_bat-1, change, cur+1)
        if min_value > change:  # 무조건 일단 교체하기
            find_chage(battery, battery[cur]-1, change+1, cur+1)
import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    station = list(map(int, input().split()))
    battery = station[1:]
    min_value = 10000
    find_chage(battery, battery[0], 0, 0)
    print(min_value)