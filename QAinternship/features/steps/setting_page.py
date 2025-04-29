from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Verify the right page opens')
def verify_page_opens(context):
    context.app.setting_page.verify_url('settings')


@then('Verify the “connect the company” button is available')
def verify_page_connect_btn(context):
    context.app.setting_page.verify_connect_btn()

@then('Verify there are {options_amount}options for the settings')
def verify_page_options(context, options_amount):
    context.app.setting_page.verify_page_options(options_amount)




