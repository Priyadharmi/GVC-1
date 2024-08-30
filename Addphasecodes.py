import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://gvcqa.adcuratio.net/login")

driver.find_element(By.XPATH, "//input[@id='email']").send_keys("shubhi.trivedi@adcuratio.com")
driver.find_element(By.ID, "password").send_keys("Adcuratio@123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)
editprojectkickoffbtn = driver.find_element(By.XPATH, "//span[text()='Edit Project Kick Off'][1]")
editprojectkickoffbtn.click()
time.sleep(10)
#def Addphasecodes():
for i in range(1, 13):
    assignphasecodesbtn = driver.find_element(By.XPATH, "(//span[text()='+ Add Labor Code'])[{i}]")
    assignphasecodesbtn.click()
    time.sleep(5)

    laborcodebtn = driver.find_element(By.XPATH, "//div[@class='projectKickoff_code__VHurS']")
    if laborcodebtn.is_displayed():
        laborcodebtn.click()
        closebtn = driver.find_element(By.CSS_SELECTOR,
                                           "svg[viewBox='64 64 896 896'][focusable='false'][data-icon='close-circle']")
        closebtn.click()
        break
    else:
            closebtn = driver.find_element(By.CSS_SELECTOR,
                                           "svg[viewBox='64 64 896 896'][focusable='false'][data-icon='close-circle']")
            closebtn.click()
            time.sleep(5)

driver.quit()