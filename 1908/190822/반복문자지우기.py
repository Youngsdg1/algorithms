import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    text = input()

    def delete(t):
        j = 0
        semi_t = t
        for i in range(len(t)):
            j += 1
            if j < len(t):
                if t[i] == t[j]:
                    new_t = t[:j - 1] + t[j + 1:]
                    return delete(new_t)
        else:
            return semi_t
    print('#{} {}'.format(tc, len(delete(text))))