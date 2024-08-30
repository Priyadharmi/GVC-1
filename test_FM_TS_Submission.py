import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ZTC2 import handle_ZTC
from ZTC2 import submit_normal_timesheet
from selenium.common.exceptions import NoSuchElementException


def test_fm_ts_submission():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gvcqa.adcuratio.net/login")

    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("akshay.kumar@adcuratio.com")
    driver.find_element(By.ID, "password").send_keys("Adcuratio@123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
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


    # projectbtn = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-search'])[1]")
    # projectbtn.click()
    # time.sleep(5)
    # projectselectionbtn = driver.find_element(By.XPATH, "//div[@title='ProjectGvcQATest2']")
    # projectselectionbtn.click()
    # startDateandtime = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Date Time'])[1]")))
    # startDateandtime.send_keys('2024-07-03 12:01 AM')
    # startDateandtime.send_keys(Keys.ENTER)
    # time.sleep(5)
    # enddateandtime = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Date Time'])[2]")))
    # enddateandtime.send_keys('2024-07-03 01:00 AM')
    # enddateandtime.send_keys(Keys.ENTER)
    # time.sleep(5)
    # phasecodeselbtn = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "(//span[@class='ant-select-selection-search'])[2]")))
    # time.sleep(5)
    # phasecodeselbtn.click()
    # phasebtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@title='GENERAL CONDITIONS']")))
    # phasebtn.click()
    # time.sleep(10)
    # laborcodeselbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ant-select-selection-search'])[3]")))
    # laborcodeselbtn.click()
    # time.sleep(5)
    # laborcodebtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@title='PROJECT MANAGER']")))
    # laborcodebtn.click()
    # time.sleep(5)
    # hrsbtn = driver.find_element(By.XPATH, "//input[@placeholder='00:00']")
    # hrsbtn.send_keys('00:59')
    # hrsbtn.send_keys(Keys.ENTER)
    # time.sleep(5)
    # legalquestionbtn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-radio'])[1]")))
    # legalquestionbtn1.click()
    # time.sleep(2)
    # legalquestionbtn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-radio'])[2]")))
    # legalquestionbtn2.click()
    # time.sleep(2)
    # legalquestionbtn3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-radio'])[3]")))
    # legalquestionbtn3.click()
    # time.sleep(2)
    # checkboxbtn = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    # checkboxbtn.click()
    # time.sleep(2)
    # submitbtn = driver.find_element(By.XPATH, "//span[text()='Submit']")
    # submitbtn.click()
    # confirmationbtn = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//div[text()='Yes']")))
    # confirmationbtn.click()
    # time.sleep(15)
    # print("TS submitted successfully")
    # driver.quit()