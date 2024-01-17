number = int(input())

for current_message in range(number):
    current_number = int(input())
    message = ""
    if current_number == 88:
        message = "Hello"
    elif current_number == 86:
        message = "How are you?"
    elif current_number < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(message)
