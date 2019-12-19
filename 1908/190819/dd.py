s = 'Reverse this strings'
print(''.join(reversed(s)))
#인덱스 루프, 리버스, 슬라이싱

print(s[::-1])

res = []
for i in range(1, len(s)+1):
    res.append(s[-i])
print(''.join(res))