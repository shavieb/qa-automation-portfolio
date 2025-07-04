from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart():
    service = Service("/users/shavieb/downloads/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        # Login
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Add first item
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
        item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()

        # Go to cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

        assert item_name == cart_item, "❌ Item in cart does not match!"
        print("✅ Test Passed: Item added to cart successfully.")

    except Exception as e:
        print("❌ Test Failed:", e)
    finally:
        driver.quit()

# Run the test
test_add_to_cart()
