type_1 = [1, 2, 3, 4, 5]
type_2 = [2, 1, 2, 3, 2, 4, 2, 5]
type_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    scores = [[0, -1], [0, -2], [0, -3]]
    types = [type_1, type_2, type_3]

    for i, answer in enumerate(answers):
        for j in range(len(types)):
            if types[j][i % len(types[j])] == answer:
                scores[j][0] += 1

    scores.sort(reverse=True)
    max_score = scores[0][0]

    result = []

    for score, idx in scores:
        idx = -idx
        if score == max_score:
            result.append(idx)
        else:
            break

    return result
