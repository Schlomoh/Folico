from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)

from resources.locators import locators
from resources.data import Data
from resources.mobile_emulation import setup

driver = webdriver.Firefox
class BaseOp():
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text, web_element.text + 'should be' + element_text

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    
    def mobile_mode(self, driver, activate):
        if activate == True:
            setup.mobi_emu(self, driver)

    def bigger_than(self, by_locator, value):
        if by_locator > value : 
            return True
        else: 
            return False

    def smaller_than(self, by_locator, value):
        if by_locator < value:
            return True
        else:
            return False

    def visibility_check(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def make_tag_url(self, tag):
        tag_url = Data.EXPLORE_TAGS + tag + '/'
        print('Hashtag used: {} URL generated: {}'.format(tag, tag_url))
        return tag_url
      