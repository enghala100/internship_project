from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingPage(Page):
 CONNECT_BTN=(By.XPATH,'//div[text()="Connect the company"]')
 SETTINGS_MENU_OPTIONS=(By.CSS_SELECTOR, "div.settings-block-menu a")

 def verify_url(self, expected_url):
     self.verify_partial_url(expected_url)

 def verify_connect_btn(self):
     self.click(*self.CONNECT_BTN)



 def verify_page_options(self, options_amount):
     options_amount = int(options_amount)  # Convert from string to integer
     self.wait_until_visible(*self.SETTINGS_MENU_OPTIONS)
     actual_options_count =len(self.driver.find_elements(*self.SETTINGS_MENU_OPTIONS))
     assert actual_options_count >= options_amount, (
         f"Expected {options_amount} options, but found {actual_options_count}")