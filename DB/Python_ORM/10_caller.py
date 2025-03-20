import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order
from decimal import Decimal
from django.db.models import Q, F, Count, Case, When, Value


def populate_db():
    # Create test profiles
    profile1 = Profile.objects.create(
        full_name="Adam Smith",
        email="adam.smith@example.com",
        phone_number="123456789",
        address="123 Main St, Springfield",
        is_active=True
    )

    profile2 = Profile.objects.create(
        full_name="Susan James",
        email="susan.james@example.com",
        phone_number="987654321",
        address="456 Elm St, Metropolis",
        is_active=True
    )

    # Create test products
    product1 = Product.objects.create(
        name="Desk M",
        description="A medium-sized office desk",
        price=Decimal("150.00"),
        in_stock=10,
        is_available=True
    )

    product2 = Product.objects.create(
        name="Display DL",
        description="A 24-inch HD display",
        price=Decimal("200.00"),
        in_stock=5,
        is_available=True
    )

    product3 = Product.objects.create(
        name="Printer Br PM",
        description="A high-speed printer",
        price=Decimal("300.00"),
        in_stock=3,
        is_available=True
    )

    # Create test orders
    order1 = Order.objects.create(
        profile=profile1,
        total_price=Decimal("1699.98"),
        is_completed=False
    )
    order1.products.add(product1, product3)

    order2 = Order.objects.create(
        profile=profile2,
        total_price=Decimal("999.99"),
        is_completed=True
    )
    order2.products.add(product1, product3, product2)

    profile1.order_profile.add(order1, order2)
    profile2.order_profile.add(order2)


def get_profiles(search_string=None):
    if search_string is None:
        return ""

    profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string)
        |
        Q(phone_number__icontains=search_string)
        |
        Q(email__icontains=search_string)
    ).order_by("full_name")

    return '\n'.join(
        f"Profile: {p.full_name}, email: {p.email}, "
        f"phone number: {p.phone_number}, "
        f"orders: {p.order_profile.count()}" for p in profiles
    )


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    return '\n'.join(f"Profile: {p.full_name}, orders: {p.orders_count}" for p in profiles)


def get_last_sold_products():
    last_order = Order.objects.prefetch_related('products').last()

    if last_order is None or not last_order.products.exists():
        return ""

    products_names = [p.name for p in last_order.products.all()]
    return f"Last sold products: {', '.join(products_names)}"


def get_top_products():
    top_products = Product.objects.annotate(
        sold_count=Count('order_products')
    ).filter(
        sold_count__gt=0
    ).order_by(
        '-sold_count',
        'name'
    )[:5]

    if not top_products.exists():
        return ""

    return "Top products:\n" + "\n".join(
        f"{p.name}, sold {p.sold_count} times"
        for p in top_products
    )


def apply_discounts():
    updated_orders_count = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2,
        is_completed=False
    ).update(
        total_price=F('total_price') * 0.90
    )

    return f"Discount applied to {updated_orders_count} orders."


def complete_order():
    order = Order.objects.filter(
        is_completed=False
    ).order_by(
        'creation_date'
        ).first()

    if order is None:
        return ""

    # Not that optimized solution
    for p in order.products.all():
        p.in_stock -= 1

        if p.in_stock == 0:
            p.is_available = False

        p.save()

    return "Order has been completed!"


