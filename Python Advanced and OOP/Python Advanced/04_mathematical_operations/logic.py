def mathematical_operations(num1, sign, num2):
    if sign == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return 'Cannot divide by zero!'
    elif sign == '*':
        return num1 * num2
    elif sign == '-':
        return num2 - num1
    elif sign == '+':
        return num1 + num2
    elif sign == '^':
        return num1 ** num2
