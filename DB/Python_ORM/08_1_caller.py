import os
import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from decimal import Decimal
# from main_app.models import ...


# # Test code for Task 1
#
#
# customer = Customer(
#     name="Svetlin Nakov1",
#     age=1,
#     email="nakov@example",
#     phone_number="+35912345678",
#     website_url="htsatps://nakov.com/"
# )
#
# try:
#     customer.full_clean()
#     customer.save()
# except ValidationError as e:
#     print('\n'.join(e.messages))


# Output

# Name can only contain letters and spaces
# Age must be greater than or equal to 18
# Enter a valid email address
# Phone number must start with '+359' followed by 9 digits
# Enter a valid URL


# # Test code for Task 2
#
# book = Book(
#     title="Short Title",
#     description="A book with a short title.",
#     genre="Fiction",
#     author="A",
#     isbn="1234"
# )
#
# try:
#     book.full_clean()
#     book.save()
#
# except ValidationError as e:
#     print("Validation Error for Book:")
#     for field, errors in e.message_dict.items():
#         print(f"{field}: {', '.join(errors)}")


# Output

# Validation Error for Book:
# author: Author must be at least 5 characters long
# isbn: ISBN must be at least 6 characters long


# # Test code for Task 3
#
# # Create a Product instance
# product = Product.objects.create(name="Gaming Keyboard", price=Decimal(100.00))
#
# # Calculate and print the tax
# tax_price = product.calculate_tax()
# print(f"Tax for {product.name}: ${tax_price:.2f}")
#
# # Calculate and print the shipping cost
# shipping_cost = product.calculate_shipping_cost(Decimal(2.50))
# print(f"Shipping Cost for {product.name}: ${shipping_cost:.2f}")
#
# # Format and print the product name
# formatted_name = product.format_product_name()
# print(f"Formatted Product Name: {formatted_name}")
# # Create a DiscountedProduct instance
# discounted_product = DiscountedProduct.objects.create(name="Gaming Mouse", price=Decimal(120.00))
#
# # Calculate and print the price without discount (DiscountedProduct)
# discounted_price = discounted_product.calculate_price_without_discount()
# print(f"Price Without Discount for {discounted_product.name}: ${discounted_price:.2f}")
#
# # Calculate and print the tax (DiscountedProduct)
# tax_price = discounted_product.calculate_tax()
# print(f"Tax for {discounted_product.name}: ${tax_price:.2f}")
#
# # Calculate and print the shipping cost (DiscountedProduct)
# shipping_cost = discounted_product.calculate_shipping_cost(Decimal(2.50))
# print(f"Shipping Cost for {discounted_product.name}: ${shipping_cost:.2f}")
#
# # Format and print the product name (DiscountedProduct)
# formatted_name = discounted_product.format_product_name()
# print(f"Formatted Product Name: {formatted_name}")


# Output

# Tax for Gaming Keyboard: $8.00
# Shipping Cost for Gaming Keyboard: $5.00
# Formatted Product Name: Product: Gaming Keyboard
# Price Without Discount for Gaming Mouse: $144.00
# Tax for Gaming Mouse: $6.00
# Shipping Cost for Gaming Mouse: $3.75
# Formatted Product Name: Discounted Product: Gaming Mouse


# # Test code for Task 4
#
# # Create instance of SpiderHero
# spiderman = SpiderHero(name="Spider-Man", hero_title="Spider Hero", energy=100)
#
# # Create instance of FlashHero
# flash = FlashHero(name="The Flash", hero_title="Flash Hero", energy=70)
#
# # Save the instances to the database
# spiderman.save()
# flash.save()
#
# # Run the special abilities
# print(spiderman.swing_from_buildings())
# print(flash.run_at_super_speed())
# print(spiderman.swing_from_buildings())
#
# # Recharge the energy of Spider-Man and The Flash using the mixin method
# spiderman.recharge_energy(195)
# flash.recharge_energy(40)
#
# # Now you can check the updated energy levels
# print(f"{spiderman.name} - Energy: {spiderman.energy}")
# print(f"{flash.name} - Energy: {flash.energy}")


# Output


# Spider-Man as Spider Hero swings from buildings using web shooters
# The Flash as Flash Hero runs at lightning speed, saving the day
# Spider-Man as Spider Hero is out of web shooter fluid
# Spider-Man - Energy: 100
# The Flash - Energy: 45

