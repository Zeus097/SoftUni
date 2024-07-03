from project.product import Product
from typing import List, Optional


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        return next((p for p in self.products if p.name == product_name), None)

    def remove(self, product_name) -> None:
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        collection = []
        for product in self.products:
            collection.append(f"{product.name}: {product.quantity}")

        return "\n".join(collection)
