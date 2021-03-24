from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


CHANGE_PHOTO = (By.CSS_SELECTOR, "span[class='edit-gravatar__label']")


@Then ("Verify that change photo icon clickable")
def verify_change_photo_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(CHANGE_PHOTO))