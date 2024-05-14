algebraic_expression = input()
parentheses_collection = []

for index in range(len(algebraic_expression)):
    if algebraic_expression[index] == '(':
        parentheses_collection.append(index)
    elif algebraic_expression[index] == ')':
        open_parentheses = parentheses_collection.pop()
        close_parentheses = index
        print(algebraic_expression[open_parentheses:close_parentheses + 1])
