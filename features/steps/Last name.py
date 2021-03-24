from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


LAST_NAME = (By.ID, "last_name")


@When ("Put {last_name} in 'Last name' field")
def click_on_the_last_name(context,last_name):
    global l_name
    l_name = last_name
    last_name_field = context.driver.find_element(*LAST_NAME)
    last_name_field.click()
    last_name_field.clear()
    last_name_field.send_keys(last_name)


@Then("Verify last name saved successfully!")
def verify_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(LAST_NAME))
    context.driver.refresh()
    check_last_name = context.driver.find_element(*LAST_NAME)
    assert check_last_name.get_attribute("value") == l_name, f"Expected {l_name} but got {check_last_name.get_attribute('value')}"