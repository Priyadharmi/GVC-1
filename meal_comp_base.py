import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import driver



    # Login to the application
def meal_comp_base(driver):

        projectbtn = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-search'])[1]")
        projectbtn.click()
        time.sleep(5)
        projectselectionbtn = driver.find_element(By.XPATH, "//div[@title='ProjectGvcQATest2']")
        projectselectionbtn.click()
        startDateandtime = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Date Time'])[1]")))
        startDateandtime.send_keys('2024-07-08 09:00 PM')
        startDateandtime.send_keys(Keys.ENTER)
        time.sleep(5)
        enddateandtime = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Date Time'])[2]")))
        enddateandtime.send_keys('2024-07-09 03:00 AM')
        enddateandtime.send_keys(Keys.ENTER)
        time.sleep(5)
        Lunchtogglebtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='ant-switch-inner'])[2]")))
        Lunchtogglebtn.click()
        time.sleep(10)
        Lunchstarttime = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Time'])[1]")))
        Lunchstarttime.send_keys('03:00 AM')
        Lunchstarttime.send_keys(Keys.ENTER)
        time.sleep(10)

        try:

            # Find the element using the text content
            MealComp1Eligiblebtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='You are eligible for Meal Comp 1']")))

            # Check if the element is present
            if MealComp1Eligiblebtn.is_displayed():
                print("Element with text 'You are eligible for Meal Comp 1' is present")
            else:
                print("Element with text 'You are eligible for Meal Comp 1' is not present")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Meal comp TC is executed")

        # Lunchendtime = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Time'])[2]"))
        # )
        # Lunchendtime.clear()
        # Lunchstarttime.clear()
        # Lunchstarttime.send_keys('07:00 AM')
        # Lunchstarttime.send_keys(Keys.ENTER)

        driver.quit()