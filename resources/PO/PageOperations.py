from selenium import webdriver
from resources.PO.BaseOperations import BaseOp
from resources.locators import locators
from resources.data import Data
from resources.mobile_emulation import setup

class LoginPage(BaseOp):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        LOGIN_URL = Data.BASE_URL + 'Login/'
        self.driver.get(LOGIN_URL)
        while self.visibility_check(locators.LOGIN_BUTTON):
            self.enter_text(locators.USERNAME_BOX, Data.USERNAME)
            self.enter_text(locators.PASSWORD_BOX, Data.PASSWORD)
            self.click(locators.LOGIN_BUTTON)

    
class ExplorePage(BaseOp):
    def __init__(self, driver):
        super.__init__(driver)
        self.driver.get(Data.EXPLORE)

    def click_first_expl_post(self):
        self.click(locators.FIRST_EXPLORE_POST)

class ExploreTagsPage(BaseOp):
    def __init__(self, driver):
        super.__init__(driver)

    def get_tag_page(self, tag):
        current_url = self.make_tag_url(tag)
        self.driver.get(current_url)

    def check_tag_name(self, tag):
        name = '#' + locators.TAG_NAME
        self.assert_element_text(name, tag)

    def click_similar_tag(self, number):
        self.click(locators.SIMILAR_TAG(self, number))

    def click_first_tag_post(self):
        self.click(locators.FIRST_TAG_POST)

class PostPage(BaseOp):
    def __init__(self, driver):
        super.__init__(driver)

    def next_post(self):
        self.click(locators.RIGHT_BUTTON)

    def previous_post(self):
        self.click(locators.LEFT_BUTTON)
    
    def like(self):
        self.click(locators.LIKE_BUTTON)

    def read_likes(self):
        amount = locators.LIKE_COUNT
        return amount
    
    def read_username(self):
        current_user = locators.USERNAME
        return current_user

    def click_more_button(self):
        self.click(locators.MORE_BUTTON)
        
class ProfilePage(BaseOp):
    def __init__(self,driver):
        super.__init__(driver)

    def go_back(self):
        self.click(locators.BACK_BUTTON)

    def click_follow(self):
        self.click(locators.FOLLOW_BUTTON)

    def read_post_count(self):
        count = locators.POST_COUNT
        return count
        
    def read_subscriber_count(self):
        count = locators.SUBSCRIBER_COUNT
        return count

    def read_subscribed_count(self):
        count = locators.SUBSCRIBED_COUNT
        return count
    
    def read_bio(self):
        bio = locators.BIO_TEXT
        return bio

    def click_first_prof_post(self):
        self.click(locators.FIRST_PROFILE_POST)