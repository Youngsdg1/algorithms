container = list()
trucks = list()
chk = [0] * n
res = 0

def findmax(arr):
    max = max(arr)
    i = arr.index(max)
    arr[i]  = 0
    return max

while 1:
    c = findmax(container)
    cur = findmax(trucks)
    if c ==0 or cur == 0:
        break
    if c > cur:
        while c > cur:
            cur = findmax(container)
            if c <= cur:
                res += cur
    else:
        res += cur

