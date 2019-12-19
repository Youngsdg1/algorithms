import sys
import copy
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    pan, change_str = input().split()
    arr = [int(i) for i in pan]
    res = []
    for k in range(int(change_str)):
        for i in range(len(pan)-1):
            for j in range(i, len(pan)):
                shallow = copy.deepcopy(arr)
                shallow[i], shallow[j] = shallow[j], shallow[i]
                res.append(shallow)
    print(res)
    hap = []
    for i in res:
        temp = 0
        for j in range(len(i)):
            temp += i[j]* (10**(len(i)-j-1))
        hap.append(temp)
    print('#{} {}'.format(tc, max(hap)))