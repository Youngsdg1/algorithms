import sys
sys.stdin = open("input.txt", "r")
T = int(input())
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T + 1):
    first_line = list(input().split())
    test_case = list(input().split())
    res_num = []
    for i in test_case:
        res_num.append(nums.index(i))
    res_num.sort()
    print(res_num)
    res_chr = []
    for i in res_num:
        res_chr.append(nums[i])
    print('#{}'.format(tc))
    print('{}'.format(' '.join(res_chr)))


    # 딕셔너리로 만드려면, 각각 키값이 0 인 딕셔너리를 직접 만들고
    # 돌릴때마다 키값 카운트를 하나씩 돌려서 갯수를 세어주고.
    # num + ' ' 를 count[i]한거 만큼 곱해준다
    # result += 한  result를 print한다. [:-1] 은 마지막 공백을 빼주기위함
    # 또는 j in sorted string 이고 for k, v in numbers.items() 이면 v ==j: result.append(k) 이런식으로.
    nums = {"ZRO" : 0, "ONE" : 0, "TWO" : 0, "THR" : 0, "FOR" : 0, "FIV" : 0, "SIX" : 0, "SVN" : 0, "EGT" : 0, "NIN" : 0}
    
    for i in range(N):
        count[dict[slist[i]]] += 1
        str = ""

        for i in range(10):
            for _ in range(count[i]):
                str += temp[i]
                str += ""

