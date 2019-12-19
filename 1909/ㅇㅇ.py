N = 105
if N < 18:
    start = 1
else:
    start = N-(len(str(N)))*9

flag = True
while flag:
    dsum = start
    for n in str(start):
        dsum += int(n)

    if dsum == N:
        flag = False
    else:
        if dsum > N: # 생성자가 없는 경우
            start = 0
            flag = False
        else:
            start += 1

print(start)