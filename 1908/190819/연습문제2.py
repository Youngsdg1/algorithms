# itoa() 구현하기. 숫자를 문자로 바꾸기
# ord 는 문자열에 대한 아스키 코드값을 알려준다.
# print(ord('0'))
#
# s = str(input())
#
# s = list(map(int,input().split()))  # 숫자
# res = []
# for i in range(len(s)):
#     ch = 48 + s[i]
#     ans = chr(ch)
#     res.append(ans)
#
# print(' '.join(res))
# print(type(ans))
def atoi(str):
    value = 0

    for i in range(len(str)):
        if ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
            digit = ord(str[i]) - ord('0')
        else:
            break

        value = (value * 10) + digit
    return value

print(atoi('5876'))

def myitoa(x):
    sr = ''
    while True:
        r = x % 10  # 나머지
        sr = sr + chr(r + ord('0'))
        x //= 10  # 123 들어오면 321 저장됨 ahrt
        if x == 0:
            break

    s = ''
    for i in range(len(sr) -1, -1, -1):  # 역으로 저장
        s = s + sr[i]
    return s

print(myitoa(1234))