class EmailValidator:
    def __init__(self, min_length: int, mails: str, domains: str):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email) -> bool:
        left_half = email.split('@')[0]
        second_half = email.split('@')[1]

        name = left_half
        mail = second_half.split('.')[0]
        domain = second_half.split('.')[1]

        return (self.__is_name_valid(name) and
                self.__is_mail_valid(mail) and
                self.__is_domain_valid(domain))


# Test code

# mails = ["gmail", "softuni"]
# domains = ["com", "bg"]
# email_validator = EmailValidator(6, mails, domains)
# print(email_validator.validate("pe77er@gmail.com"))
# print(email_validator.validate("georgios@gmail.net"))
# print(email_validator.validate("stamatito@abv.net"))
# print(email_validator.validate("abv@softuni.bg"))
