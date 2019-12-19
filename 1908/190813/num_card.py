import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    num_of_cards = int(input())
    cards = list(map(int, input()))
    cards_list = [0] * 10

    for i in range(len(cards)):
        cards_list[cards[i]] += 1
        max_count = max(cards_list)

    for i in range(len(cards_list)):
        if cards_list[i] == max_count:
            max_num = i

    print('#{} {} {}'.format(test_case, max_num, max_count))

