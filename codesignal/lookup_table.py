MAX_NUMBER = 1_000_000


def sol(numbers):
    power_of_2s = []
    available_numbers = [-1] * (2 * MAX_NUMBER)

    for i, number in enumerate(numbers):
        available_numbers[number + MAX_NUMBER] = i

    power = 0

    while 2**power <= 2 * MAX_NUMBER:
        power_of_2s.append(2**power)
        power += 1
    power_of_2s.append(2**power)

    res = 0
    for power_of_2 in power_of_2s:
        for i, number in enumerate(numbers):
            idx = power_of_2 - number + MAX_NUMBER
            if idx < 0 or len(available_numbers) <= idx:
                continue

            if available_numbers[idx] == -1:
                continue

            if available_numbers[idx] >= i:
                res += 1
    return res


print(sol([1, -1, 2, 3]))
print(sol([2]))
print(sol([-2, -1, 0, 1, 2]))
