

t = [0]*6
def p(k, n):
    global t
    if k == n:
        print(t)
    else:
        for i in range(k, n+1):
            t[k] = i
            p(k+1, n)
n = [1, 2, 3, 4, 5, 6]
# p(0, 6)

def powersetlist(li):

    r = [[]]
    for l in li:
        temp = [x+[l] for x in r]
        r += temp

    return r

print(powersetlist(n))

def powerset(li):
    r = [[]]
    for l in li:
        for x in r:
            temp = [x+[l]]
            r += temp
    return r

print(powerset(n))