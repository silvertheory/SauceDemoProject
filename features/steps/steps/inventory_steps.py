from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")

    def validate_products(self):
        for item in self.get_products():
            assert item.find_element(By.CLASS_NAME, "inventory_item_name").is_displayed()
            assert item.find_element(By.CLASS_NAME, "inventory_item_price").is_displayed()
            img = item.find_element(By.CLASS_NAME, "inventory_item_img").find_element(By.TAG_NAME, "img")
            assert img.is_displayed()
            assert item.find_element(By.TAG_NAME, "button").is_displayed()

@given("I am on the SauceDemo login page")
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service('./chromedriver.exe'))
    context.driver.get("https://www.saucedemo.com/")

@when('I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

@then('each product should display a name, price, image, and add-to-cart button')
def step_impl(context):
    page = InventoryPage(context.driver)
    page.validate_products()
    context.driver.quit()
