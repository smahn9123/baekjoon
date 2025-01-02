str_n = input()
n = int(str_n)


def get_digit_sum(number):
    return number + sum(int(i) for i in str(number))


answer = 0
for i in range(max(0, n - 9 * len(str_n)), n):
    if get_digit_sum(i) == n:
        answer = i
        break

print(answer)
