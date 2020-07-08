from base.Selenium_driver import Selenium_driver


class TestStatus(Selenium_driver):

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultlist = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("pass")
                    self.log.info("sdfghj")

                else:
                    self.resultlist.append("fail")
                    self.log.error("sdfghj")
                    self.screenshot(resultMessage)
            else:
                self.resultlist.append("fail")
                self.log.error("sdfghj")
                self.screenshot(resultMessage)
        except:
            self.resultlist.append("fail")
            self.screenshot(resultMessage)

    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markfinal(self, testname, result, resultMessage):

        self.setResult(result, resultMessage)
        if "fail" in self.resultlist:
            self.log.error(testname + "  tets fail")
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info(testname + "    tests sucessfull")
            self.resultlist.clear()
            assert True == True
