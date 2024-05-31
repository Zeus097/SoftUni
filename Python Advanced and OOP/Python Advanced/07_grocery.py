def grocery_store(**kwargs):
    recipe = ''
    sorted_recipe = dict(sorted(kwargs.items(), key=lambda kwp: (-kwp[1], -len(kwp[0]), kwp[0])))

    for product_name, quantity in sorted_recipe.items():
        recipe += f'{product_name}: {quantity}\n'

    return recipe


# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))


# print(grocery_store(
#     bread=2,
#     pasta=2,
#     eggs=20,
#     carrot=1,
# ))
