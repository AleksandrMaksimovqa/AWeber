from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

FIRST_NAME = (By.ID, "first_name")
SAVE_PROFILE_BUTTON = (By.CSS_SELECTOR, "button[type = 'submit']")
NOTICE_ICON = (By.ID, "notices")


@Given ("Open wordpress profile page")
def open_wordpress(context):
    context.driver.get("https://wordpress.com/me")
    username = context.driver.find_element(By.ID, "usernameOrEmail")
    username.click()
    username.send_keys("aleksandrmaksimovqa@gmail.com")
    context.driver.find_element(By.CSS_SELECTOR, "button[type]").click()
    password = context.driver.find_element(By.ID, "password")
    password.click()
    password.send_keys("y6Pb$Qx+hzs_N)w")
    context.driver.find_element(By.CSS_SELECTOR, "button[class = 'button form-button is-primary']").click()


@When("Put {first_name} in 'First name' field")
def click_on_first_name(context,first_name):
    global f_name
    f_name = first_name
    first_name_field = context.driver.find_element(*FIRST_NAME)
    first_name_field.click()
    first_name_field.clear()
    first_name_field.send_keys(first_name)


@Then("Click on the 'Save profile details' button")
def click_on_save_profile_button(context):
    save_profile = context.driver.find_element(*SAVE_PROFILE_BUTTON)
    context.driver.wait.until(EC.element_to_be_clickable(SAVE_PROFILE_BUTTON))
    save_profile.click()


@Then("Verify first name saved successfully!")
def verify_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(FIRST_NAME))
    context.driver.refresh()
    check_first_name = context.driver.find_element(*FIRST_NAME)
    assert check_first_name.get_attribute("value") == f_name, f"Expected {f_name} but got {check_first_name.get_attribute('value')}"