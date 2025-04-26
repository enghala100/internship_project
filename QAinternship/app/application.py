from pages.base_page import Page
from pages.main_page import MainPage
from pages.login_page import LogInPage
from pages.setting_page import SettingPage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = Page(driver)
        self.login_page = LogInPage(driver)
        self.main_page = MainPage(driver)
        self.setting_page = SettingPage(driver)

