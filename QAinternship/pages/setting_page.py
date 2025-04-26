from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingPage(Page):
 CONNECT_BTN=(By.XPATH,'//div[text()="Connect the company"]')
 SETTINGS_MENU_OPTIONS=(By.CSS_SELECTOR, "div.settings-block-menu a")

 def verify_url(self, expected_url):
     self.verify_partial_url(expected_url)

 def verify_connect_btn(self):
     self.click(*self.CONNECT_BTN)

 def get_menu_options_count(self):
     self.wait_until_visible(*self.SETTINGS_MENU_OPTIONS)
     return len(self.driver.find_elements(*self.SETTINGS_MENU_OPTIONS))