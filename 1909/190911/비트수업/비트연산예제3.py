# 0xff 는 1로 다 채워진거

n = 0x00111111  # 16진수니까 2진수로 0001
print(0xff)
if n & 0xff:  # 끝에 1이 있는 위치만 나옴. f = 15 니까 비트로 쓰면 1111 이 됨
    print('little endian')
    # 1이 있는데만 비트가 나옴
else:
    print('big endian')