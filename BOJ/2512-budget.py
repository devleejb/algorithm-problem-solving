N = int(input())
budget_list = list(map(int, input().split()))
target_budget = int(input())
budget_sum = sum(budget_list)


def calc_budget(max_val):
    sum = 0

    for budget in budget_list:
        if (budget > max_val):
            sum += max_val
        else:
            sum += budget

    return sum


if (budget_sum <= target_budget):
    print(max(budget_list))
else:
    start = 1
    end = max(budget_list)
    max_val = end

    while start <= end:
        mid = (start + end) // 2

        budget = calc_budget(mid)

        if (budget > target_budget):
            end = mid - 1
        else:
            max_val = mid
            start = mid + 1

    print(max_val)
