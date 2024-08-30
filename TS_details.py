import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def TS_details():
    projectbtn = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-search'])[1]")
    projectbtn.click()
    time.sleep(5)
    projectselectionbtn = driver.find_element(By.XPATH, "//div[@title='ProjectGvcQATest2']")
    projectselectionbtn.click()
    startDateandtime = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Date Time'])[1]")))
    startDateandtime.send_keys('2024-06-22 12:00 AM')
    startDateandtime.send_keys(Keys.ENTER)
    time.sleep(5)
    enddateandtime = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Date Time'])[2]")))
    enddateandtime.send_keys('2024-06-22 02:00 AM')
    enddateandtime.send_keys(Keys.ENTER)
    time.sleep(5)
    phasecodeselbtn = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-search'])[2]")
    time.sleep(5)
    phasecodeselbtn.click()
    phasebtn = driver.find_element(By.XPATH, "//div[@title='GRADE']")
    time.sleep(5)
    phasebtn.click()
    laborcodeselbtn = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-search'])[3]")
    time.sleep(5)
    laborcodeselbtn.click()
    laborcodebtn = driver.find_element(By.XPATH, "//div[@title='EXCAVATION LABOR']")
    laborcodebtn.click()
    time.sleep(5)
    hrsbtn = driver.find_element(By.XPATH, "//input[@placeholder='00:00']")
    hrsbtn.send_keys('02:00')
    hrsbtn.send_keys(Keys.ENTER)
    time.sleep(5)
    legalquestionbtn1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@class='ant-radio-input' and @type='radio'])[1]")))
    legalquestionbtn1.click()
    legalquestionbtn2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@class='ant-radio-input' and @type='radio'])[1]")))
    legalquestionbtn2.click()
    time.sleep(2)
    checkboxbtn = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkboxbtn.click()
    submitbtn = driver.find_element(By.XPATH, "//span[text()=' Submit']")
    submitbtn.click()
