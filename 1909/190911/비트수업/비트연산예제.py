def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):  # 7부터 0까지
        output += "1" if i & (1 << j) else "0"
        print(output)

for i in range(-7, 6):
    print("%3d = " % i, end='')
    Bbit_print(i)

    # 1의 보수를 만들때 5의 비트에서 1에 대한 보수를 만들고, 거기에 마지막 1만 더한것이 -5임.
    # 5 = 00000101
    # 1의보수 = 11111010
    # 2의보수 = 1의보수 + 1 = 11111011
