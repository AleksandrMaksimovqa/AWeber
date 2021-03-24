from behave import Given, When, Then
from selenium.webdriver.common.by import By


CANCEL_BUTTON = (By.CSS_SELECTOR, "button[class *= 'cancel form']")



@Then("Click 'Cancel' button")
def click_add_site_button(context):
    cancel_button = context.driver.find_element(*CANCEL_BUTTON)
    cancel_button.click()