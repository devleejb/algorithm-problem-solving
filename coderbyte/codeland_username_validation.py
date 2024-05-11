def is_valid_length(username):
    return 4 <= len(username) <= 25


def is_letter(c: str):
    return ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z")


def is_number(c: str):
    return ord("0") <= ord(c) <= ord("9")


def CodelandUsernameValidation(username: str) -> bool:
    # The username is between 4 and 25 characters.
    if not is_valid_length(username):
        return False

    # It must start with a letter.
    if not is_letter(username[0]):
        return False

    # It cannot end with an underscore character.
    if username[-1] == "_":
        return False

    # It can only contain letters, numbers, and the underscore character.
    for c in username:
        if not (is_number(c) or is_letter(c) or c == "_"):
            return False

    return True


# keep this function call here
print(CodelandUsernameValidation(input()))
