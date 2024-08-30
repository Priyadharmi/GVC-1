import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from datetime import datetime
import time

def handle_ZTC(driver):
    try:
        # Wait for the "Review" element to be present
        ZTC = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Review']")))
        ZTC.click()
        time.sleep(5)

        # Example: Perform actions on the ZTC page
        # Replace with your specific actions
        legalq1 = driver.find_element(By.XPATH, "(//input[@type='radio'])[7]")
        legalq1.click()
        legalq2 = driver.find_element(By.XPATH, "(//input[@type='radio'])[9]")
        legalq2.click()
        legalq3 = driver.find_element(By.XPATH, "(//input[@type='radio'])[11]")
        legalq3.click()
        checkboxbtn = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
        checkboxbtn.click()
        submittsbtn = driver.find_element(By.XPATH, "//span[text()='Submit Time Sheet']")
        submittsbtn.click()

        # Handle confirmation dialog
        yesbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Yes']")))
        yesbtn.click()
        time.sleep(10)


        return True  # Successfully processed a ZTC

    except NoSuchElementException:
        print("No more ZTCs")
        return False  # No more ZTCs found

    except Exception as e:
        print(f"Error occurred while processing ZTC: {str(e)}")
        return False  # Error encountered while processing ZTC

def submit_normal_timesheet(driver):
    try:
        # Example: Select project
        projectbtn = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-search'])[1]")
        projectbtn.click()
        time.sleep(5)
        projectselectionbtn = driver.find_element(By.XPATH, "//div[@title='ProjectGvcQATest2']")
        projectselectionbtn.click()

        # Example: Enter start date and time
        startDateandtime = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Date Time'])[1]")))
        startDateandtime.send_keys('2024-07-04 02:01 AM')
        startDateandtime.send_keys(Keys.ENTER)
        time.sleep(5)

        # Example: Enter end date and time
        enddateandtime = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Date Time'])[2]")))
        enddateandtime.send_keys('2024-07-04 03:00 AM')
        enddateandtime.send_keys(Keys.ENTER)
        time.sleep(5)

        # Example: Select phase code
        phasecodeselbtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='ant-select-selection-search'])[2]")))
        time.sleep(5)
        phasecodeselbtn.click()
        phasebtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@title='GENERAL CONDITIONS']")))
        phasebtn.click()
        time.sleep(10)

        # Example: Select labor code
        laborcodeselbtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='ant-select-selection-search'])[3]")))
        laborcodeselbtn.click()
        time.sleep(5)
        laborcodebtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@title='PROJECT MANAGER']")))
        laborcodebtn.click()
        time.sleep(5)

        # Example: Enter hours
        hrsbtn = driver.find_element(By.XPATH, "//input[@placeholder='00:00']")
        hrsbtn.send_keys('00:59')
        hrsbtn.send_keys(Keys.ENTER)
        time.sleep(5)

        # Example: Answer legal questions
        legalquestionbtn1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-radio'])[1]")))
        legalquestionbtn1.click()
        time.sleep(2)
        legalquestionbtn2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-radio'])[2]")))
        legalquestionbtn2.click()
        time.sleep(2)
        try:
            legalquestionbtn3 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//span[@class='ant-radio'])[3]")))
            legalquestionbtn3.click()

            checkboxbtn = driver.find_element(By.XPATH, "//input[@type='checkbox']")
            checkboxbtn.click()
            time.sleep(2)

            # Example: Submit timesheet
            submitbtn = driver.find_element(By.XPATH, "//span[text()='Submit']")
            submitbtn.click()
        except TimeoutException:
            print("Element not found")
            time.sleep(2)

            checkboxbtn = driver.find_element(By.XPATH, "//input[@type='checkbox']")
            checkboxbtn.click()
            time.sleep(2)

            # Example: Submit timesheet
            submitbtn = driver.find_element(By.XPATH, "//span[text()=' Submit']")
            submitbtn.click()



        # Handle confirmation dialog
        confirmationbtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Yes']")))
        confirmationbtn.click()
        time.sleep(15)

        print("Normal timesheet submitted successfully")

    except Exception as e:
        print(f"Error occurred while submitting normal timesheet: {str(e)}")

# def main():
#
#         try:
#             # Initialize WebDriver
#             driver = webdriver.Chrome()
#             driver.maximize_window()
#
#             # Navigate to login page and login
#             driver.get("https://gvcqa.adcuratio.net/login")
#             driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test_foreman1@gvc.com")
#             driver.find_element(By.ID, "password").send_keys("Adcuratio@123")
#             driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
#             time.sleep(10)  # Wait for initial page load
#
#             # Handle multiple ZTCs
#             while handle_ZTC(driver):
#                 pass  # Continue handling ZTCs until none are left
#             time.sleep(10)
#
#             # Once all ZTCs are handled, submit normal timesheet
#             submit_normal_timesheet(driver)
#
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")
#
#             # driver.quit()  # Close the WebDriver session
#
#
#
#         finally:
#             driver.quit()  # Close the WebDriver session
#
# if __name__ == "__main__":
#         main()
