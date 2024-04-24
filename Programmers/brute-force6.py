alphabets = ["A", "E", "I", "O", "U"]
answer = 0


def dfs(target_word, word, nums):
    global answer
    if word == target_word:
        answer = nums

    if len(word) == 5:
        return nums

    for alphabet in alphabets:
        nums = dfs(target_word, word + alphabet, nums + 1)

    return nums


def solution(word):
    dfs(word, "", 0)
    return answer
