def password_validator(password):
    error_found = []

    if not 6 <= len(password) <= 10:
        error_found.append("Password must be between 6 and 10 characters")

    if not password.isalnum():
        error_found.append("Password must consist only of letters and digits")

    if (sum(character.isdigit() for character in password) < 2):
        error_found.append("Password must have at least 2 digits")

    if error_found:
        for errors in error_found:
            print(errors)
    else:
        print("Password is valid")

user_passord = input()
password_validator(user_passord)
