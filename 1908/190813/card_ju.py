def run_test_case(func):
    case_count = int(input())
    for num in range(case_count):
        input_count = int(input())
        input_list = list(input())
        input_list = list(map(int, input_list))
        result = func(input_count, input_list)
        print('#{} '.format(num+1), end='')
        print(result)
def func(input_count, input_list):
    dict = {}
    for num in range(10):
        dict[num] = input_list.count(num)
    max_v = max(dict.values())
    max_k = 0
    for k, v in dict.items():
        if v == max_v:
            max_k = k
    return '{} {}'.format(max_k, max_v  )
run_test_case(func)

