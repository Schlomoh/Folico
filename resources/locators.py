from selenium.webdriver.common.by import By

class locators():

#--- Login Page Locators ---#
    USERNAME_BOX = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_BOX = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

#--- Explore Tags Locators --#
    TAG_NAME = (By.XPATH, "//*[@id='react-root']/section/nav[1]/div/header/div/h1")
    FIRST_TAG_POST = (By.XPATH, "//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a")
    
    def SIMILAR_TAG(self, number):
        STAG = "//*[@id='react-root']/section/main/div/div/span[2]/div["+ str(number) +"]"
        SIMTAG = (By.XPATH, STAG)
        return SIMTAG
        
#--- Post Locators ---#
    RIGHT_BUTTON = (By.XPATH, "/html/body/div[4]/div[1]/div/div/a[2]")
    LEFT_BUTTON = (By.XPATH, "/html/body/div[4]/div[1]/div/div/a[1]")
    LIKE_BUTTON = (By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
    LIKE_COUNT = (By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/a/span")
    USERNAME = (By.XPATH, "/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a")
    MORE_BUTTON = (By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/div[1]/div[1]/div/span/span[2]/button")
    POST_DESCRIPTION = (By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/div[1]/div[1]/div/span/span")
    TIME_STAMP = (By.XPATH, "/html/body/div[5]/div[2]/div/article/div[2]/div[2]/a/time")

#--- Profile Page Locators ---#
    BACK_BUTTON = (By.XPATH, "//*[@id='react-root']/section/nav[1]/div/header/div/div[1]/a")
    FOLLOW_BUTTON = (By.XPATH, "//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
    POST_COUNT = (By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span")
    SUBSCRIBER_COUNT = (By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span")
    SUBSCRIBED_COUNT = (By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span")
    BIO_TEXT = (By.XPATH, "//*[@id='react-root']/section/main/div/header/section/div[2]/span")
    FIRST_PROFILE_POST = (By.XPATH, "//*[@id='react-root']/section/main/div/div[2]/article/div/div/div[1]/div[1]/a")

#--- Explore Page Locators ---#
    FIRST_EXPLORE_POST = (By.XPATH, "//*[@id='react-root']/section/main/div/div[2]/div/div[1]/div[2]/div/a")