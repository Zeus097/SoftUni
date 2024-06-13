from logic import mathematical_operations


text_input = input().split()
number_1, operator, number_2 = text_input
operation = mathematical_operations(float(number_1), operator, int(number_2))
print(f'{operation:.2f}')
