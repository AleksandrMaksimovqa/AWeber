from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


ICON = (By.ID, "notices")


@Then("Verify icon appears")
def verify_saved_icon_appears(context):
    context.driver.wait.until(EC.presence_of_element_located(ICON))