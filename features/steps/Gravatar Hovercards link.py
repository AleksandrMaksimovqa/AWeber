from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


GRAVATAR_HOVERCARDS_LINK = (By.CSS_SELECTOR, "a[href *= 'gravatar-hover']")


@Then("Click on 'Gravatar Hovercards' link")
def verify_gravatar_hovervards_links(context):
    gravatar_hovervards_link = context.driver.find_element(*GRAVATAR_HOVERCARDS_LINK)
    gravatar_hovervards_link.click()
    context.driver.wait.until(EC.new_window_is_opened)