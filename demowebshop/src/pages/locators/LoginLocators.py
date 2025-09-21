
from selenium.webdriver.common.by import By

class LoginLocators:

    LOGIN_HEADER_BTN = (By.CLASS_NAME, "ico-login")
    LOGIN_EMAIL = (By.ID, "Email")
    LOGIN_PASSWORD = (By.ID, "Password")
    LOGIN_BTN = (By.CSS_SELECTOR, 'input[value="Log in"]')

    SUCCESS_LOGIN_VERIFICATION = (By.CSS_SELECTOR, 'div.header-links li a.ico-logout')
    INVALID_LOGIN_EMAIL_ERROR_MSG = (By.CSS_SELECTOR, 'div.validation-summary-errors span')