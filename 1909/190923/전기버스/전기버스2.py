def bt(stop, count):
    global mn
    global Ms
    if count >= mn:
        return

    new_battery = Ms[stop]
    if stop + new_battery >= N-1:
        mn = min(mn, count)
        return
    for battery_usage in range(new_battery, -1, -1):
        bt(stop+battery_usage, count+1)
import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    data = list(map(int, input().split()))
    N = data[0]
    mn = data[:-1]
    print(mn)
    bt(0, 0)
    print(mn)