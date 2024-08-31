from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage

class LoginPage(BasePage):
    # Initialize the Elements in the HOme page
    NAME_INPUT = (By.CSS_SELECTOR,".form-control")
    #NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD =(By.ID,"exampleInputPassword1")
    CHECK_BOX = (By.ID, "exampleCheck1")
    RADIO_BUTTON = (By.NAME,"inlineRadioOptions")
    EMPLOYMENT_STATUS = (By.XPATH,"//label[contains(text(),'Student')]")
    SHOP_LINK = (By.LINK_TEXT, "Shop")
    GENDER_OPTION = (By.XPATH,"//select[@id='exampleFormControlSelect1']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")


    def enter_name(self, name):
        self.enter_text(self.NAME_INPUT, name)

    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, pwd):
            self.enter_text(self.PASSWORD, pwd)

    def navigate_to_shop(self):
        self.click(self.SHOP_LINK)

    def select_gender(self, gender):
        self.select_dropdown(self.CHECK_BOX,gender)

    def select_emplystatus(self,status):
        self.find_element(self.RADIO_BUTTON)
        self.click(self.EMPLOYMENT_STATUS)



