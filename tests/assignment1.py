import pytest
from pages.search_results_page import SearchResultsPage
from models.product import Product
from models.shopping_cart import ShoppingCart

def test_add_item_to_shopping_cart():
    # Assuming loblawsPage is already initialized and available here
    query = 'apple'
    resultsPage = loblawsPage.search(query)
    productInCart = resultsPage.get_product_info_by_index(1)
    cart = resultsPage.add_item_to_shopping_cart(1)
    inCartProdName = cart.get_product_name_at(1)
    inCartProdPrice = cart.get_product_price_at(1)

    # Using pytest's assert statement for comparison and error messages
    assert inCartProdName == productInCart.get_product_name(), "Names should match"
    assert abs(inCartProdPrice - productInCart.get_selling_price_now().get_value()) < 0.001
