
from selenium.webdriver.common.by import By

class AddProductsToWishlistLocators:

    PRODUCT_CARD = (By.CSS_SELECTOR, "div.product-item div.picture")
    ADD_TO_WISHLIST_BTN = (By.CSS_SELECTOR, 'input[value="Add to wishlist"]')
    WISHLIST_ELEMENT_LINK = (By.CSS_SELECTOR, 'li a.ico-wishlist span.cart-label')
    PRODUCT_NAME_IN_WISHLIST = (By.CSS_SELECTOR, 'tr td.product')

