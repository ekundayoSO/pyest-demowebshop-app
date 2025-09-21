import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class SeleniumExtended:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator)
        ).click()

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator)).send_keys(text)

    def wait_until_element_is_visible(self, locator_or_element, timeout=None):
        timeout = timeout or self.default_timeout
        elem = WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator_or_element)
        )
        return elem

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(ec.text_to_be_present_in_element(locator, text))

    def wait_and_input_text_and_click_enter(self, locator, text, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator)).send_keys(text, Keys.ENTER)
        time.sleep(1)

    def wait_and_get_elements(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        elements = WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))
        return elements

    def wait_select_dropdown(self, locator, to_select, select_by='visible_text'):
        select_element = self.wait_until_element_is_visible(locator)
        select = Select(select_element)
        if select_by.lower() == 'visible_text':
            select.select_by_visible_text(to_select)
        elif select_by.lower() == 'index':
            select.select_by_index(to_select)
        elif select_by.lower() == 'value':
            select.select_by_value(to_select)
        else:
            raise Exception(
                f"Invalid option for 'to_select' parameter. Valid values are 'visible_text', 'index', or value 'value'.")

