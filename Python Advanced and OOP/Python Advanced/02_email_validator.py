class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    command = input()
    if command == 'End':
        break

    current_email = command

    if '@' not in current_email:
        raise MustContainAtSymbolError("Email must contain @")

    name = current_email.split('@')[0]
    current_domain = current_email.split('.')[-1]
    valid_domains = ['.com', '.bg', '.net', '.org']

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if ("." + current_domain) not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
