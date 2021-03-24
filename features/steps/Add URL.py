from behave import Given, When, Then
from selenium.webdriver.common.by import By


ADD_BUTTON = (By.CSS_SELECTOR, "button[class='button is-compact']")
ADD_URL_AND_WORDPRESS_BUTTON = (By.CSS_SELECTOR,"button.popover__menu-item")
ENTER_URL = (By.CSS_SELECTOR, "input[placeholder= 'Enter a URL']")
ENTER_DISCRIPTION = (By.CSS_SELECTOR,"input[placeholder= 'Enter a description']")
ADD_SITE_BUTTON = (By.CSS_SELECTOR, "button[class *= 'add form']")


@When("Click on 'Add' button")
def click_on_add_button(context):
    add_button = context.driver.find_element(*ADD_BUTTON)
    add_button.click()


@When("Click on 'Add URL' button")
def click_on_add_url_button(context):
    add_url = context.driver.find_elements(*ADD_URL_AND_WORDPRESS_BUTTON)[1]
    add_url.click()


@Then("Enter {url} and {description}")
def enter_url_and_description(context,url,description):
    enter_url = context.driver.find_element(*ENTER_URL)
    enter_url.click()
    enter_url.clear()
    enter_url.send_keys(url)
    enter_description = context.driver.find_element(*ENTER_DISCRIPTION)
    enter_description.click()
    enter_description.clear()
    enter_description.send_keys(description)


@Then("Click 'Add site' button")
def click_add_site_button(context):
    add_site_button = context.driver.find_element(*ADD_SITE_BUTTON)
    add_site_button.click()