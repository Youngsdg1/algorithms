# 부분집합 찾아보고
# process_sol 에서 합이 10이면 출력되게 하고
# 가지치기에서 값이 10보다 크면 짜르는 조건 추가
def process_solution(a, k):
    sum = 0
    for i in range(1, 11):
        if a[i] == True:
            sum += i
    if sum == 10:
        for i in range(1, 11):
            if a[i] == True:
                print(i, end=' ')
        print()

def backtrack(a, k, input):  # input = depth
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):  # 선택 됐는지 안됐는지 보기 위해 T, F로 들어감
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
print(backtrack(a, 0, 10))