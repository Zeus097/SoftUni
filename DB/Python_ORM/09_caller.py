import os
import django
from django.db.models import Sum, Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


def product_quantity_ordered():
    products = Product.objects.annotate(
        total_quantity=Sum('orderproduct__quantity')
    ).exclude(
        total_quantity=None
    ).order_by('-total_quantity')

    return '\n'.join(f"Quantity ordered of {p.name}: {p.total_quantity}" for p in products)


def ordered_products_per_customer():
    prefetched_orders = Order.objects.prefetch_related('orderproduct_set__product__category').order_by('id')
    result = []

    for order in prefetched_orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")
        for order_product in order.orderproduct_set.all():
            result.append(f"- Product: {order_product.product.name}, Category: {order_product.product.category.name}")

    return '\n'.join(result)


def filter_products():
    query = Q(is_available=True) & Q(price__gt=3.00)
    products = Product.objects.filter(query).order_by('-price', 'name')
    return '\n'.join(f"{p.name}: {p.price}lv." for p in products)


def give_discount():
    reduction = F('price') * 0.70
    query = Q(is_available=True) & Q(price__gt=3.00)
    Product.objects.filter(query).update(price=reduction)
    all_available_products = Product.objects.filter(is_available=True).order_by('-price', 'name')

    products_ls = []
    for product in all_available_products:
        products_ls.append(f"{product.name}: {product.price}lv.")

    return '\n'.join(products_ls)


