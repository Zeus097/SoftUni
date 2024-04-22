text = input()
parentheses = []

for index in range(len(text)):
    if text[index] == '(':
        parentheses.append(index)
    elif text[index] == ')':
        start_index = parentheses.pop()
        end_index = index + 1
        print(text[start_index:end_index])
