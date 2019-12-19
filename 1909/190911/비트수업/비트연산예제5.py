def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)
a = 0x86  # 1000 0110 (8(8,4,2,1) 6(4,2)) 2의 4배승 이니까 4비트씩 모으면 16진수가 됨
key = 0xAA  # A가 10 이니까 2, 8 해서 1010 1010 (10, 10)

print('key    ==> ', end='')
Bbit_print(key)

print('a      ==> ', end='')
Bbit_print(a)

print('a^=key ==> ', end='')
a ^= key
Bbit_print(a)

print('a^=key ==> ', end='')
a ^= key
Bbit_print(a)