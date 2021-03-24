from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


YOUR_PROFILE_LINK = (By.CSS_SELECTOR, "a[href *= 'gravatar.com']")


@Then("Click on 'your profile' link")
def verify_profile_links(context):
    profile_link = context.driver.find_element(*YOUR_PROFILE_LINK)
    profile_link.click()
    context.driver.wait.until(EC.new_window_is_opened)