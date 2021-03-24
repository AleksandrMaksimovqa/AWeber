from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


PUBLIC_DISPLAY_NAME = (By.ID, "display_name")


@When ("Put {display_name} in 'Public display name' field")
def click_on_the_last_name(context,display_name):
    global d_name
    d_name = display_name
    last_name_field = context.driver.find_element(*PUBLIC_DISPLAY_NAME)
    last_name_field.click()
    last_name_field.clear()
    last_name_field.send_keys(display_name)


@Then("Verify Public display name saved successfully!")
def verify_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(PUBLIC_DISPLAY_NAME))
    context.driver.refresh()
    check_last_name = context.driver.find_element(*PUBLIC_DISPLAY_NAME)
    assert check_last_name.get_attribute("value") == d_name, f"Expected {d_name} but got {check_last_name.get_attribute('value')}"