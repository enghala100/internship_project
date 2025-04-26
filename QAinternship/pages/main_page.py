from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):


 SETTING_BTN=(By.CSS_SELECTOR,'div.settings-code')


 def click_settings(self):
     self.click(*self.SETTING_BTN)