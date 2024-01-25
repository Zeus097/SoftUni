first_string = input()
second_string = input()
third_string = input()
first_string, third_string = third_string, first_string
animal_body = [first_string, second_string, third_string]

print(animal_body)


# second_solution
#
# tail = input()
# body = input()
# head = input()
# meerkat = [tail, body, head]
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
#
# print(meerkat)
