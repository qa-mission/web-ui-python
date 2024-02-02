from typing import List, Dict
from product import Product  # Assuming you have a Product class


class Catalogue:
    def __init__(self, products: List[Product]):
        self.products = products
        self.container = self.fill_container(self.products)

    def fill_container(self, products: List[Product]) -> Dict[str, Product]:
        return {p.get_id(): p for p in products}

    def sort_products_desc(self) -> List[Product]:
        sorted_products = sorted(self.products, reverse=True)
        return sorted_products

    def get_product_by_id(self, id: str) -> Product:
        if id in self.container:
            return self.container[id]
        raise RuntimeError(f"Catalogue does not have a product with ID {id}")
