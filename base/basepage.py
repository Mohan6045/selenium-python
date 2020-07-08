from base.Selenium_driver import Selenium_driver
from utilities.util import Util


class BasePage(Selenium_driver):
    def __init__(self,driver):
        super(BasePage,self).__init__(driver)
        self.util = Util()

    def verifypageTile(self,titleToverify):
        try :
            actual_tile = self.getTitle()
            return  self.util.veriftextContains(actual_tile,titleToverify)
        except:
            self.log.error("failed to get page ")
            return False
