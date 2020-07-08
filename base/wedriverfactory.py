from selenium import webdriver


class WebdriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl = "https://www.saucedemo.com"
        if self.browser == "chrome":
            driver = webdriver.Chrome(executable_path="/Users/mohan/Documents/Driver/chromedriver")
        elif self.browser == "FF":
            driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver
