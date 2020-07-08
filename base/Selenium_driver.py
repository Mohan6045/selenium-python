import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import csv

class Selenium_driver():

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, resultmessage):
        filename = resultmessage+ " "+str(round(time.time()*1000)) + ".png"
        screendshotDirectory ="../screenshot/"
        relativeFilename= screendshotDirectory + filename
        currentdirectory = os.path.dirname(__file__)
        destinationfile = os.path.join(currentdirectory,relativeFilename)
        destinationdirectory = os.path.join(currentdirectory,screendshotDirectory)
        try:
            if not os.path.exists(destinationdirectory):
                os.makedirs(destinationdirectory)
            self.driver.save_screenshot(destinationfile)
            self.log.info("screen shot sucessfull")
        except:
            self.log.error("screen shot sucessfull")
            print_stack()

    def getElementlist(self,locator,locatortype="id"):
        element =None
        try:
            locatortype=locatortype.lower()
            bytype =self.getByType(locatortype)
            element = self.driver.find_elements(bytype,locator)
        except:
            print("element not found")
        return  element



    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        else:
            print("locator is not supported")
        return False

    def getElement(self, locator, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("element found")
        except:
            print("element not found")
        return element

    def ElementClick(self, locator="", locatortype="id",element = None):
        try:
            if locator:
                element = self.getElement(locator, locatortype)
            element.click()
            print("element found")
        except:
            print("cannot find click element")
            print_stack()

    def sendkeys(self, data, locator="", locatortype="id",element = None):
        try:
            if locator:
                element = self.getElement(locator, locatortype)
            element.send_keys(data)
            print("element found")
        except:
            print("cannot send data to that element")

    def isElementPresent(self, locator, locatortype="id"):
        element = None
        try:
            element = self.getElement(locator,locatortype)
            return element
        except:
            print("element not found")
            return element

    def elementPresentCheck(self, locator, byType):
        try:
            element = self.driver.find_elements(byType, locator)
            if len(element) > 0:
                print("element found")
                return True
            else:
                return False
        except:
            print("element not found")
            return False

    def waitForElement(self, locator="opentab", locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            print("enterd try block")
            byType = self.hw.getByType(locatorType)
            print("entered handy wrapper")
            print(byType)
            wait = WebDriverWait(self.driver, 10)
            print(wait)
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
        except:
            print("element not found")
            print_stack()
        return element
