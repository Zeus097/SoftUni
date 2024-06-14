def cookbook(*args):
    result = ''
    cook_book = {}
    for book in args:
        recipe_name, cuisine, ingredients = book
        if cuisine not in cook_book:
            cook_book[cuisine] = {}
        cook_book[cuisine][recipe_name] = ingredients

    sorted_cook_book = sorted(cook_book.items(), key=lambda x: (-len(x[1]), x[0]))
    for recipe, current_cuisine in sorted_cook_book:
        current_recipe_count = len(current_cuisine)
        result += f"{recipe} cuisine contains {current_recipe_count} recipes:\n"
        for current_recipe_name in sorted(current_cuisine):
            result += f"  * {current_recipe_name} -> Ingredients: {', '.join(current_cuisine[current_recipe_name])}\n"

    return result.strip()


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))
#
# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))
