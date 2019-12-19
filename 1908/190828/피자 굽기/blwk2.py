import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza = []
    fire = []

    # 화덕 안의 피자
    # 화덕 밖의 피자
    # pop, append