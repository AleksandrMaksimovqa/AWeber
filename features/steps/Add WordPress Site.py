from behave import Given, When, Then
from selenium.webdriver.common.by import By


ADD_URL_AND_WORDPRESS_BUTTON = (By.CSS_SELECTOR,"button.popover__menu-item")
CHECK_BOX = (By.CSS_SELECTOR, "input[name='site-191030033']")
ADD_SITE_BUTTON = (By.CSS_SELECTOR, "form.profile-links-add-wordpress button[class *= 'primary']")


@When("Click on 'Add WordPress Site' button")
def click_on_add_wordpress_button(context):
    add_wordpress = context.driver.find_elements(*ADD_URL_AND_WORDPRESS_BUTTON)[0]
    add_wordpress.click()


@Then("Click on checkbox")
def click_on_check_box(context):
    check_box = context.driver.find_element(*CHECK_BOX)
    check_box.click()


@Then("Click 'Add sites' button")
def click_add_site_button(context):
    add_site_button = context.driver.find_element(*ADD_SITE_BUTTON)
    add_site_button.click()