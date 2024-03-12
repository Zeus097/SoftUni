def length_validation(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def character_validation(name):
    for character in name:
        if not(character.isalnum() or character == '-' or character == '_'):
            return False
    return True


def redundance_validation(name):
    if ' ' in name:
        return False
    return True


def is_valid(name):
    if length_validation(name) and character_validation(name) and redundance_validation(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if is_valid(username):
        print(username)
