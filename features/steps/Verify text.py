from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


ICON = (By.ID, "notices")


@Then("Verify text")
def verify_saved_icon_appears(context):
    icon = context.driver.find_element(*ICON)
    assert icon.text == 'Settings saved successfully!', f'Expected "Settings saved successfully!", but got {icon.text}'