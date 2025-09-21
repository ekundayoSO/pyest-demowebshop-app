import pytest
from demowebshop.src.pages.AddProductsToCartPage import AddProductsToCartPage


@pytest.mark.usefixtures("init_driver")
class TestAddItemsToCart:

    @pytest.mark.tcid4
    def test_add_products_to_cart(self):
        cart = AddProductsToCartPage(self.driver)

        # Navigate to homepage
        cart.go_to_homepage()

        # Search products and add to cart
        items = ['Smartphone', 'Computing and Internet', '14.1-inch Laptop', 'Blue Jeans']
        for item in items:
            cart.search_item_and_click_enter(item)
            cart.add_items_to_cart()
            cart.bar_notification_visible()

        # Click shopping cart element
        cart.click_cart_element()

        # verify products are added to cart
        product_names = cart.get_all_product_names_in_cart()
        assert len(product_names) == 4, f"Expected 1 item in cart, but found {len(product_names)}"
