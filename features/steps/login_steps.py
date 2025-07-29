from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

@given('I am on the SauceDemo login page')
def step_open_login(context):
    service = Service('./chromedriver.exe')
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://www.saucedemo.com/")

@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)  # Give time for page to load

@then('I should see the inventory page')
def step_verify_inventory(context):
    assert "inventory" in context.driver.current_url, "Did not reach inventory page"
    context.driver.quit()

@then('I should see a login error message')
def step_see_error_message(context):
    try:
        error = context.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error.is_displayed()
        print("Error message displayed: PASSED")
    except NoSuchElementException:
        assert False, "Error message NOT displayed!"
    finally:
        context.driver.quit()

    @then('I should see a locked out error message')
    def step_locked_out_error(context):
        try:
            error = context.driver.find_element(By.XPATH, "//h3[@data-test='error']")
            assert "locked out" in error.text.lower()
        except NoSuchElementException:
            assert False, "Locked out error message not found!"
        finally:
            context.driver.quit()

    @given('I am logged in as "{username}" with password "{password}"')
    def step_logged_in(context, username, password):
        service = Service('./chromedriver.exe')
        context.driver = webdriver.Chrome(service=service)
        context.driver.get("https://www.saucedemo.com/")
        context.driver.find_element(By.ID, "user-name").send_keys(username)
        context.driver.find_element(By.ID, "password").send_keys(password)
        context.driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

    @then('I should see 6 products on the inventory page')
    def step_six_products(context):
        items = context.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(items) == 6, f"Expected 6 products, found {len(items)}"
        context.driver.quit()

    @then('each product should display a name, price, image, and add-to-cart button')
    def step_check_product_elements(context):
        items = context.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(items) > 0, "No products found"
        for item in items:
            # Name
            name = item.find_element(By.CLASS_NAME, "inventory_item_name")
            assert name.is_displayed(), "Product name missing"
            # Price
            price = item.find_element(By.CLASS_NAME, "inventory_item_price")
            assert price.is_displayed(), "Product price missing"
            # Image
            img = item.find_element(By.CLASS_NAME, "inventory_item_img")
            assert img.find_element(By.TAG_NAME, "img").is_displayed(), "Product image missing"
            # Add to cart button
            btn = item.find_element(By.TAG_NAME, "button")
            assert btn.is_displayed(), "Add to cart button missing"
        context.driver.quit()

