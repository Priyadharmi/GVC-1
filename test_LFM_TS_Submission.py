import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from TS_details import TS_details
from ZTC2 import handle_ZTC
from ZTC2 import submit_normal_timesheet

def test_lfm_ts_submission():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gvcqa.adcuratio.net/login")

    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("charles.boyle@adcuratio.com")
    driver.find_element(By.ID, "password").send_keys("Adcuratio@123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
    #TS_details()

    try:

        while handle_ZTC(driver):
            pass  # Continue handling ZTCs until none are left
            time.sleep(10)

    # Once all ZTCs are handled, submit normal timesheet
        submit_normal_timesheet(driver)


    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()
