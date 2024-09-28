def calc_vowel_or_consonants(letter):
    vowels = ["a", "e", "i", "o", "u", "y"]

    if letter in vowels:
        return "0"
    else:
        return "1"


def sol(pattern, source):
    coverted_pattern = []

    for s in source:
        coverted_pattern.append(calc_vowel_or_consonants(s))

    result = 0

    for i in range(len(coverted_pattern) - len(pattern) + 1):
        sub_converted_pattern = "".join(coverted_pattern[i : i + len(pattern)])
        if sub_converted_pattern == pattern:
            result += 1

    return result


print(sol("010", "amazing"))
