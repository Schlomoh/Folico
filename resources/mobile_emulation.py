from selenium import webdriver as driver

class setup():
    def __init__(self, driver):
        self.driver = driver
    
    def mobi_emu(self, driver):
        user_agent = (
            "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15"
            "(KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1 "
        )
        profile = driver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)
        driver.set_window_size(375, 812)