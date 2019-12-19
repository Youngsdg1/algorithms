import sys
sys.stdin = open('input.txt', 'r')
def charge_num(battery, cur_battery, change, cur):
    global min_val
    if cur == len(battery):
        if min_val > change:
            min_val = change
    else:
        if cur_battery > 0:
            charge_num(battery, cur_battery-1, change, cur + 1)
        if min_val > change:
            charge_num(battery, battery[cur]-1, change+1, cur + 1)
for tc in range(1, int(input())+1):
    station = list(map(int, input().split()))
    battery = station[1:]
    min_val = 999999
    charge_num(battery, battery[0], 0, 0)
    print('#{} {}'.format(tc, min_val))