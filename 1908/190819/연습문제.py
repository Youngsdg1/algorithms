s = 'Reverse this strings'
print(''.join(reversed(s)))
#인덱스 루프, 리버스, 슬라이싱

print(s[::-1])

for i in range(0, len(s), -1):
    print(i)