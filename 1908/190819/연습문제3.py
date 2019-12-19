# 고지식한 패턴 알고리즘
p = 'rithm'
t = 'a pattern matching algorithm'
m = len(p)
n = len(t)

def BruteForce(p, t):
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    while j < m and i < n:
        if t[i] != p[j]:
            i = i - j
            j = - 1
        i = i + 1
        j = j + 1
    if j == m:
        return i - m
    else:
        return -1

print(BruteForce(p, t))  # 23번째 인덱스에 있다 이말이야~