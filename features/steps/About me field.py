from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


ABOUT_ME = (By.ID, "description")


@When ("Put {about_me} in 'About me' field")
def click_on_the_last_name(context,about_me):
    global ab_me
    ab_me = about_me
    last_name_field = context.driver.find_element(*ABOUT_ME)
    last_name_field.click()
    last_name_field.clear()
    last_name_field.send_keys(about_me)


@Then("Verify About me field saved successfully!")
def verify_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(ABOUT_ME))
    context.driver.refresh()
    check_last_name = context.driver.find_element(*ABOUT_ME)
    assert check_last_name.get_attribute("value") == ab_me, f"Expected {ab_me} but got {check_last_name.get_attribute('value')}"