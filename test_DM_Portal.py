import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_DM_Portal():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gvcqa.adcuratio.net/login")

    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("shubhi.trivedi@adcuratio.com")
    driver.find_element(By.ID, "password").send_keys("Adcuratio@123")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
    logoutbtn = driver.find_element(By.XPATH, "//span[contains(text(),'Logout')]")
    if logoutbtn is not None:
        print("Login Successful")

    editprojectkickoffbtn = driver.find_element(By.XPATH, "//span[text()='Edit Project Kick Off'][1]")
    editprojectkickoffbtn.click()
    time.sleep(10)
    time.sleep(5)
    assignphasecodesbtn = driver.find_element(By.XPATH, "//div[11]//div[1]//button[1]//span[1]")
    assignphasecodesbtn.click()
    time.sleep(5)

    laborcodebtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='projectKickoff_code__VHurS']")))
    laborcodebtn.click()
    time.sleep(5)

    closebtn = driver.find_element(By.CSS_SELECTOR,"svg[viewBox='64 64 896 896'][focusable='false'][data-icon='close-circle']")
    closebtn.click()
    time.sleep(5)
    perdiembtn = driver.find_element(By.XPATH,
                                     "//body/div[@id='root']/section[@class='ant-layout ant-layout-has-sider main-layout css-w8mnev']/section[@class='ant-layout css-w8mnev']/main[@class='ant-layout-content css-w8mnev']/div[@class='mainContent_contentMain__924Bf']/div[@class='projectKickoff_accordionContainer__3-UWq']/div[3]/button[1]/span[1]")
    perdiembtn.click()
    time.sleep(5)

    fuelallowancebtn = driver.find_element(By.XPATH,
                                           "//body/div[@id='root']/section[@class='ant-layout ant-layout-has-sider main-layout css-w8mnev']/section[@class='ant-layout css-w8mnev']/main[@class='ant-layout-content css-w8mnev']/div[@class='mainContent_contentMain__924Bf']/div[@class='projectKickoff_accordionContainer__3-UWq']/div[4]/button[1]/span[1]")
    fuelallowancebtn.click()
    time.sleep(5)

    savebtn = driver.find_element(By.XPATH, "//span[normalize-space()='Save']")
    savebtn.click()
    time.sleep(5)

    Assignbtn = driver.find_element(By.XPATH, "//span[normalize-space()='Assign']")
    Assignbtn.click()
    time.sleep(2)

    Updatebtn = driver.find_element(By.XPATH, "//span[normalize-space()='Update']")
    Updatebtn.click()
    time.sleep(15)

    savebtn = driver.find_element(By.XPATH, "//span[normalize-space()='Save']")
    savebtn.click()
    time.sleep(5)

    Assignbtn = driver.find_element(By.XPATH, "//span[normalize-space()='Assign']")
    Assignbtn.click()
    time.sleep(10)

    Addbtn = driver.find_element(By.XPATH, "//span[normalize-space()='+ Add']")
    Addbtn.click()
    time.sleep(180)

    Cmbtn = driver.find_element(By.CSS_SELECTOR,
                                "#root > section > section > main > div > div > div.manageProject_viewContainer__d8rNS > div:nth-child(2) > div > div.addScreen_tabContent__\+lOYd > div > div:nth-child(3) > div > div:nth-child(53)")
    Cmbtn.click()

    assignbtn = driver.find_element(By.XPATH, "//span[text()='Assign']")
    assignbtn.click()
    time.sleep(10)

    viewbtn = driver.find_element(By.XPATH, "//button[@class='tabContainer_active__NBYUC']")
    if viewbtn is not None:
        print("Added people,Phase and labor codes successfully")

    driver.quit()
