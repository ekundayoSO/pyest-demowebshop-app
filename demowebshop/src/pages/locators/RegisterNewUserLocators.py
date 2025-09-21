
from selenium.webdriver.common.by import By

class RegisterNewUserLocators:

    GENDER_BUTTON = (By.ID, "gender-male")
    FIRST_NAME_FIELD = (By.ID, "FirstName")
    LAST_NAME_FIELD = (By.ID, "LastName")
    EMAIL_FIELD = (By.ID, "Email")
    PASSWORD_FIELD = (By.ID, "Password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")

    REGISTRATION_VERIFICATION = (By.CSS_SELECTOR, 'div.header-links li a.account')

