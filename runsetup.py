import unittest
from selenium import webdriver
from time import sleep, strftime
from random import randint

import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)

#from resources.PO.BaseOperations import BaseOp
from resources.PO.PageOperations import LoginPage, ExplorePage, ExploreTagsPage, PostPage, ProfilePage
#from resources.locators import locators
#from resources.data import Data
#from reports.users import ousers, nusers
from test.test_functions import checks

LoginPage.login()
#sleep(5)