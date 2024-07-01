class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> None:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> str:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients:
            if self.ingredients[ingredient] - quantity < 0:
                return f"Please check again the desired quantity of {ingredient}!"
            self.ingredients[ingredient] -= quantity
            self.price -= price_per_quantity * quantity
        else:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

    def make_order(self):
        self.ordered = True
        current_order = []
        ingredients_list = []
        current_order.append(f"You've ordered pizza {self.name} prepared with")
        for current_ingredient, current_quantity in self.ingredients.items():
            ingredients_list.append(f"{current_ingredient}: {current_quantity}")
        current_order.append(', '.join(ingredients_list))
        current_order.append(f"and the price will be {self.price}lv.")
        return ' '.join(current_order)


# # Test code
#
# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))
