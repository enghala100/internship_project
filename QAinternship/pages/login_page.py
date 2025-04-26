from pages.base_page import Page
from selenium.webdriver.common.by import By

class LogInPage(Page):
 EMAIL_FIELD=(By.ID,'email-2')
 PASSWORD_FIELD=(By.ID,'field')
 CONTINUE_BTN=(By.CSS_SELECTOR,'a.login-button')


 def open_main_page(self):
  self.open_url(self.base_url)



 def login(self,email,password):
  self.wait_until_visible(*self.EMAIL_FIELD)
  self.input_text(email,*self.EMAIL_FIELD)
  self.wait_until_visible(*self.PASSWORD_FIELD)
  self.input_text(password,*self.PASSWORD_FIELD)
  self.wait_until_clickable(*self.CONTINUE_BTN)
  self.click(*self.CONTINUE_BTN)
