from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from test.pages.base_page import BasePage


class ShopPage():

    PAGE_TITLE =''
    SHOP_PAGE_URL = "https://rahulshettyacademy.com/angularpractice/shop"
    ADD_BUTTONS = (By.XPATH, "//button[contains(text(),'Add')")

    def __init__(self, browser):
       self.browser = browser

    def launch_shop(self):
        self.browser.get(self.SHOP_PAGE_URL)

    def assert_shop_page_title(self):
        WebDriverWait(self.browser, 10).until(
            lambda browser: browser.title != ""
        )
        # Assert the title with a custom error message
        assert self.browser.title == "ProtoCommerce", f"Expected title to be 'ProtoCommerce', but got '{self.browser.title}'"



