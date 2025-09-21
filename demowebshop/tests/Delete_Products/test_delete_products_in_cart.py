from itertools import count

import pytest
from demowebshop.src.pages.AddProductsToCartPage import AddProductsToCartPage
from demowebshop.src.pages.DeleteProductInShoppingCartPage import DeleteProductInShoppingCartPage


@pytest.mark.usefixtures("init_driver")
class TestDeleteProductsInCart:

    @pytest.mark.tcid6
    def test_delete_products_from_cart(self):
        cart = AddProductsToCartPage(self.driver)
        delete = DeleteProductInShoppingCartPage(self.driver)

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

        # Delete products from shopping cart
        product_names = cart.get_all_product_names_in_cart()
        if "Smartphone" in product_names:
            delete.delete_single_product("Smartphone")

        # Delete only Blue Jeans if it exists
        if "Blue Jeans" in product_names:
            delete.delete_single_product("Blue Jeans")

        # Update shopping cart
        delete.update_shopping_cart()

        # Count the number of products left in the cart
        delete.count_products_left_in_shopping_cart(2)

