from demowebshop.src.pages.AddProductsToCartPage import AddProductsToCartPage
from demowebshop.src.pages.AddProductsToWishlistPage import AddProductsToWishlistPage
import pytest

@pytest.mark.usefixtures("init_driver")
class TestAddProductsToWishlist:

    @pytest.mark.tcid5
    def test_verify_products_are_added_to_wishlist(self):

        cart= AddProductsToCartPage(self.driver)
        wishlist = AddProductsToWishlistPage(self.driver)

        # Go to homepage
        cart.go_to_homepage()

        # Search and add products to watchlist
        products = ['Smartphone', 'Blue and green Sneaker']
        for product in products:
            cart.search_item_and_click_enter(product)
            wishlist.click_product_card()
            wishlist.add_products_to_wishlist()
            cart.bar_notification_visible()

        # Click watchlist element
        wishlist.click_wishlist_element()

        # Assert number of products in wishlist
        product_names = wishlist.get_all_product_names_in_wishlist()
        assert len(product_names) == 2, f"Expected 1 item in cart, but found {len(product_names)}"