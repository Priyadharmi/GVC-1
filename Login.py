import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
def Login():
 Email = driver.find_element(By.XPATH, "//input[@id='email']")
 Email.click()
 Password = driver.find_element(By.ID, "password")
 Password.click()
 Submit = driver.find_element(By.XPATH, "//button[@type='submit']")
 Submit.click()
 time.sleep(10)