from typing import List
from utils.math_utils import MathUtils  # Assuming you have a math_utils module
from price import Price


class Product:
    def __init__(self, prod_id, prod_index, sales_text, sales_ends, prod_brand, prod_name, prod_size, prod_text,
                 selling_price_now, selling_price_was, comparison_prices: List[Price]):
        self.id = prod_id
        self.productIndex = prod_index
        self.salesText = sales_text
        self.onSale = "sale" in sales_text.lower()
        self.salesEnds = sales_ends
        self.productBrand = prod_brand
        self.productName = prod_name
        self.productSize = prod_size
        self.productText = prod_text
        self.sellingPriceNow = selling_price_now
        self.sellingPriceWas = selling_price_was
        self.comparisonPrices = comparison_prices

        if self.onSale:
            if "$" in prod_text:
                self.saveValue = MathUtils.round_double(float(prod_text.split("$")[1]), 2)
            else:
                self.saveValue = 0.0
        else:
            self.saveValue = 0.0

    def __lt__(self, other):
        return self.sellingPriceNow < other.sellingPriceNow

    def get_id(self):
        return self.id

    def get_product_index(self):
        return self.productIndex

    def get_sales_text(self):
        return self.salesText

    def get_sales_ends(self):
        return self.salesEnds

    def get_product_brand(self):
        return self.productBrand

    def get_product_name(self):
        return self.productName

    def get_product_size(self):
        return self.productSize

    def get_product_text(self):
        return self.productText

    def get_selling_price_now(self):
        return self.sellingPriceNow

    def get_selling_price_was(self):
        return self.sellingPriceWas

    def get_comparison_prices(self):
        return self.comparisonPrices

    def is_on_sale(self):
        return self.onSale

    def get_save_value(self):
        return self.saveValue
