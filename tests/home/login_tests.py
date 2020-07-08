import time

from selenium import webdriver
from pages.home.login_page import Loginpage
import unittest
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("onetimeSet", "Set")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)  # py.test -v -s test_class_demo2.py --browser firefox
    def classset(self, onetimeSet):
        self.Lp = Loginpage(self.driver)
        self.ts = TestStatus(self.driver) # Assert without  stopping exeution

    def test_ValidLogin(self):
        self.Lp.login("standard_user", "secret_sauce")
        # self.ts.mark(result1,"title is incorrect")
        result = self.Lp.verifyLoginSucess()
        self.ts.markfinal("test_valid login",result,"login was succefully")
        time.sleep(5)

    # @pytest.mark.run(scope=1)
    # def test_InValidLogin(self):
    #     self.driver.get(self.baseUrl)
    #     Lp = Loginpage(self.driver)
    #     self.Lp.login("standard_user1", "secret_sauce1")
    #     result = self.Lp.verifyloginInvalid()
    #
    #     assert result == True
    #     self.driver.quit()


logintest = LoginTests()
logintest.test_ValidLogin()
