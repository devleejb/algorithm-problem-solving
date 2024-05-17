def solution(phone_book):
    answer = True
    sets = [set() for _ in range(len(phone_book))]
    phone_book.sort()
    for i, phone in enumerate(phone_book):
        cumulative = ""
        for num in list(phone):
            cumulative += num
            sets[i].add(cumulative)

    for i, phone in enumerate(phone_book[: len(phone_book) - 1]):
        if phone_book[i + 1].startswith(phone):
            answer = False

    return answer
