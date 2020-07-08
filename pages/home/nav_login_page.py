from selenium.webdriver.common.by import By
from base.Selenium_driver import Selenium_driver


class Loginpage(Selenium_driver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _email_field = "user-name"
    _password_field = "password"
    _login_Btn = "//input[@type='submit']"

    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPwdField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginBtn(self):
    #     return self.driver.find_element(By.XPATH, self._login_Btn)

    def enterEmailField(self,email):
        self.sendkeys(email,self._email_field)

    def enterPwdField(self,PWD):
        self.sendkeys(PWD,self._password_field)

    def clickLoginBtn(self):
        self.ElementClick(self._login_Btn,locatortype="xpath")

    def login(self, username, password):
        self.enterEmailField(username)
        self.enterPwdField(password)
        self.clickLoginBtn()

    def verifyLoginSucess(self):
        result = self.isElementPresent("//div[@class='product_label']",locatortype="xpath")
        return result
            #//button[@class='error-button']

    def verifyloginInvalid(self):
        result1 =self.isElementPresent("//button[@class='error-button']",locatortype="xpath")
        return result1