import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ZTC2 import handle_ZTC
from meal_comp_base import meal_comp_base
import driver

def test_meal_comp_scenario():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gvcqa.adcuratio.net/login")

    # Login
    email_input = driver.find_element(By.XPATH, "//input[@id='email']")
    email_input.send_keys("test_foreman4@gvc.com")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Adcuratio@123")

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    time.sleep(10)

    try:
        # Handle multiple ZTCs
        while handle_ZTC(driver):
            pass  # Continue handling ZTCs until none are left
        time.sleep(10)
    except Exception as e:
        print(f"Error handling ZTCs: {str(e)}")
        time.sleep(5)

    # Execute meal_comp_base function
    meal_comp_base(driver)
    driver.quit()

if __name__ == "__main__":
    test_meal_comp_scenario()
