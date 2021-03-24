from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


REMOVE_URL_BUTTON = (By.CSS_SELECTOR, "li button[class *= 'remove']")


@Then("Click on 'Remove' button")
def click_remove_url_button(context):
    remove_url_button = context.driver.find_element(*REMOVE_URL_BUTTON)
    remove_url_button.click()