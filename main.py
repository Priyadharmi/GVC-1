def main():
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    from ZTC2 import handle_ZTC
    from ZTC2 import submit_normal_timesheet
    try:
        # Initialize WebDriver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Navigate to login page and login
        driver.get("https://gvcqa.adcuratio.net/login")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test_foreman1@gvc.com")
        driver.find_element(By.ID, "password").send_keys("Adcuratio@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(10)  # Wait for initial page load

        # Handle multiple ZTCs
        while handle_ZTC(driver):
            pass  # Continue handling ZTCs until none are left
        time.sleep(10)

        # Once all ZTCs are handled, submit normal timesheet
        submit_normal_timesheet(driver)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

        #driver.quit()  # Close the WebDriver session



    finally:
        driver.quit()  # Close the WebDriver session

if __name__ == "__main__":
    main()