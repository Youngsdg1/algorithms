# 0000000111 1000000110 0000011110 0110000110 0001111001 1110011111 1001100111
# 0000000111100000011000000111100110000110000111100111100111111001100111

# def Bbit_print(i):
#     output = ""
#     for j in range(7, -1, -1):  # 7부터 0까지
#         output += 2**j if i & (1 << j) else 0
#     print(output)

input = '0000000111100000011000000111100110000110000111100111100111111001100111'
# bit = list(input.split())
# print(bit)
# for i in range(0, len(input), 7):
#     Bbit_print(i)

nums = list(''.join(input.split()))

for _ in range(10):
    result = 0
    for i in range(6, -1, -1):
        result += int(nums.pop(0)) * (1<<i)
    else:
        print(result, end=' ')