from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_remove_from_cart():
    service = Service("/users/shavieb/downloads/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open site and login
        driver.get("https://www.saucedemo.com/")
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Step 2: Add first item to cart
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()

        # Step 3: Go to cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Step 4: Remove the item
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
        driver.find_element(By.CLASS_NAME, "cart_button").click()

        # Step 5: Check that cart is empty
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 0, "❌ Cart is not empty after removing the item"

        print("✅ Test Passed: Item successfully removed from cart")

    except Exception as e:
        print("❌ Test Failed:", e)

    finally:
        driver.quit()

# Run the test
test_remove_from_cart()
