from pages.base_page import Page
from selenium.webdriver.common.by import By

class LogInPage(Page):
 EMAIL_FIELD=(By.ID,'email-2')
 PASSWORD_FIELD=(By.ID,'field')
 CONTINUE_BTN=(By.CSS_SELECTOR,'a.login-button')


 def open_main_page(self):
  self.open_url(self.base_url)



 def login(self,email,password):
  self.input_text(email,*self.EMAIL_FIELD)
  self.input_text(password,*self.PASSWORD_FIELD)
  self.click(*self.CONTINUE_BTN)
