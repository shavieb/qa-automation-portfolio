from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_form_submission():
    service = Service("/users/shavieb/downloads/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Go to DemoQA text box form
        driver.get("https://demoqa.com/text-box")

        # Step 2: Fill in the form fields
        driver.find_element(By.ID, "userName").send_keys("Shavieair Bowes")
        driver.find_element(By.ID, "userEmail").send_keys("shavieb@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("123 Automation Lane")
        driver.find_element(By.ID, "permanentAddress").send_keys("456 Selenium Ave")

        # Step 3: Click Submit
        driver.find_element(By.ID, "submit").click()

        # Step 4: Verify the confirmation box displays correct data
        name_output = driver.find_element(By.ID, "name").text
        email_output = driver.find_element(By.ID, "email").text

        assert "Shavieair Bowes" in name_output, "❌ Name not found in confirmation"
        assert "shavieb@example.com" in email_output, "❌ Email not found in confirmation"

        print("✅ Test Passed: Form submitted and confirmed correctly")

    except Exception as e:
        print("❌ Test Failed:", e)

    finally:
        driver.quit()

# Run the test
test_form_submission()
