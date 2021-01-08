from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep, strftime
from random import randint

import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)


from resources.PO.BaseOperations import BaseOp
from resources.PO.PageOperations import LoginPage, ExplorePage, ExploreTagsPage, PostPage, ProfilePage
from resources.locators import locators
from resources.data import Data
from reports.users import ousers, nusers
from resources.mobile_emulation import setup

class checks(PostPage):
    def __init__(self, driver):
        super.__init__(driver)
    
    def check_likes(self, min_limit, max_limit):
        if (self.read_likes() < min_limit) and (self.read_likes > max_limit):
           return True
        else: 
            return False

    def check_description(self, exclude=[]):
        self.click_more_button()
        description = locators.POST_DESCRIPTION
        x = 0
        c = 0
        found = False
        for c  in len(exclude):
            test = exclude[c]
            c += 1
            for x in (len(description) - len(test)):
                end = len(test) + x
                truncated = description[x:end]
                x += 1
                if truncated == test:
                    found = True
        return found            


    def check_time(self, max_time):
        Time = locators.TIME_STAMP
        print(Time)