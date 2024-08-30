import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

def Project_selection():
    projectbtn = driver.find_element(By.XPATH,  "//div[contains(@class, 'ant-select') and contains(@class, 'ant-select-single') and contains(@class, 'ant-select-show-arrow')]//input[@id='rc_select_0']")
    projectbtn.click()
    projectselectionbtn = driver.find_element(By.XPATH, "//div[contains(text(),'ProjectGvcQATest2')]")
    projectselectionbtn.click()
