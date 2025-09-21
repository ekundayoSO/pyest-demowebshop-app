import time

import pytest

from demowebshop.src.configs.products_configs import ProductsConfigs
from demowebshop.src.pages.AddProductsToCartPage import AddProductsToCartPage
from demowebshop.src.pages.CheckoutPage import CheckoutPage
from demowebshop.src.pages.CleanUpExistingContactPage import CleanUpExistingContactPage
from demowebshop.src.pages.DeleteProductInShoppingCartPage import DeleteProductInShoppingCartPage
from demowebshop.src.pages.LoginPage import LoginPage
from demowebshop.src.configs.generic_configs import GenericConfigs


@pytest.mark.usefixtures("init_driver")
class TestEndToEnd:

    @pytest.mark.tcid7
    def test_end_to_end_for_register_user(self):

        credentials = GenericConfigs()
        login_page = LoginPage(self.driver)
        cart_page = AddProductsToCartPage(self.driver)
        delete_page = DeleteProductInShoppingCartPage(self.driver)
        products_list = ProductsConfigs()
        checkout_page = CheckoutPage(self.driver)
        contact_page = CleanUpExistingContactPage(self.driver)

        # Login
        login_page.go_to_login_page()
        login_page.input_login_email(credentials.LOGIN_EMAIL)
        login_page.input_login_password(credentials.LOGIN_PASSWORD)
        login_page.click_on_login_btn()

        # Add products to shopping cart
        cart_page.go_to_homepage()
        products = products_list.products
        for product in products:
            cart_page.search_item_and_click_enter(product)
            cart_page.add_items_to_cart()
            cart_page.bar_notification_visible()
        cart_page.click_cart_element()

        # Delete products from shopping cart
        product_names = cart_page.get_all_product_names_in_cart()
        # Delete only Smartphone if it exists
        if "14.1-inch Laptop" in product_names:
            delete_page.delete_single_product("14.1-inch Laptop")

        # Delete only Blue Jeans if it exists
        if "Blue Jeans" in product_names:
            delete_page.delete_single_product("Blue Jeans")

        delete_page.update_shopping_cart()

        # Checkout
        checkout_page.click_on_service_term()
        checkout_page.click_on_checkout_btn()
        checkout_page.billing_info('Finland', 'Vantaa',
                                   'Avenue 32', '10100', '44992277')
        checkout_page.click_billing_continue_btn()
        checkout_page.shipping_info()
        checkout_page.payment_info()
        checkout_page.click_confirm_order_btn()

        # Delete existing user contact
        contact_page.delete_existing_user_contact()

