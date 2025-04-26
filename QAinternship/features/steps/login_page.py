from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.app.login_page.open_main_page()


@when('Log in to the page')
def login(context):
    context.app.login_page.login('eng.hala333@gmail.com','*******')