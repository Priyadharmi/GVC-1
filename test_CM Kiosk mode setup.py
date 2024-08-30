from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions

import driver



def test_cm_kiosk_mode():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gvcqa.adcuratio.net/login")
    time.sleep(5)
    kioskbtn = driver.find_element(By.XPATH, "(//div[@class='login_kioskModeBtn__cRdmG'])[1]")
    kioskbtn.click()
    leademailbtn = driver.find_element(By.XPATH, "//input[@id='email']")
    leademailbtn.send_keys('test_supervisor2@gvc.com')
    leadpwdbtn = driver.find_element(By.XPATH, "//input[@id='password']")
    leadpwdbtn.send_keys('Adcuratio@123')
    time.sleep(5)
    submitbtn = driver.find_element(By.XPATH, "//button[@type='submit']")
    submitbtn.click()
    time.sleep(5)
    try:
        projectbtn1 = driver.find_element(By.XPATH, "//input[@type='search']")

        projectbtn1.click()
        time.sleep(5)
        projectbtn2 = driver.find_element(By.XPATH,"//div[@class='ant-select-item-option-content' and text()='ProjectGvcQATest2']")
        projectbtn2.click()
        time.sleep(5)
        proceedbtn = driver.find_element(By.XPATH, "//span[text()='Proceed']")
        proceedbtn.click()
        time.sleep(5)
        confirmbtn = driver.find_element(By.XPATH, "//span[text()='Yes']")
        confirmbtn.click()
        time.sleep(15)
    except exceptions.NoSuchElementException:
        print("Project button not found or not enabled.")
    # Clockinbtn = driver.find_element(By.XPATH, "//span[text()='Scan Clock In']")
    # Clockinbtn.click()
    # time.sleep(5)
    # okbtn1 = driver.find_element(By.XPATH, "//span[text()='Okay']")
    # okbtn1.click()
    # time.sleep(5)
    # confirmationradio1 = driver.find_element(By.XPATH, "(//input[@type='radio'])[1]")
    # confirmationradio1.click()
    # time.sleep(5)
    # time.sleep(60)
    # Clockoutbtn = driver.find_element(By.XPATH, "//span[text()='Scan Clock Out']")
    # Clockoutbtn.click()
    # time.sleep(5)
    # okbtn2 = driver.find_element(By.XPATH, "//span[text()='Okay']")
    # okbtn2.click()
    # time.sleep(5)
    # confirmationradio2 = driver.find_element(By.XPATH, "(//input[@type='radio'])[1]")
    # confirmationradio2.click()
    # time.sleep(20)
    # selectphcodebtn = driver.find_element(By.XPATH, "//div[@class= 'timesheetTable_crewMemberTimesheet__Sd3XC']//td[1]/select")
    # selectphcodebtn.click()
    # time.sleep(6)
    # phcode = driver.find_element(By.XPATH, "//div[@class= 'timesheetTable_crewMemberTimesheet__Sd3XC']//td[1]/select/option[2]/div")
    # action_obj = ActionChains(driver)
    # action_obj.move_to_element(phcode).perform()
    # time.sleep(10)
    # phcode.click()
    #
    # time.sleep(5)
    # selectlbcodebtn = driver.find_element(By.XPATH, "//div[@class= 'timesheetTable_crewMemberTimesheet__Sd3XC']//td[2]/select")
    # selectlbcodebtn.click()
    # time.sleep(5)
    # lbcode = driver.find_element(By.XPATH, "//option[text()='SUPERVISOR']")
    # lbcode.click()
    # totalhrs = driver.find_element(By.XPATH, "(//input[@placeholder='00:00'])[3]")
    # totalhrs.send_keys('00:01')
    # legalquestionbtn1 = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[1]")))
    # legalquestionbtn1.click()
    # legalquestionbtn2 = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "((//input[@type='radio'])[2]")))
    # legalquestionbtn2.click()
    # legalquestionbtn3 = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "((//input[@type='radio'])[3]")))
    # legalquestionbtn3.click()
    # legalquestionbtn4 = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "((//input[@type='radio'])[4]")))
    # legalquestionbtn4.click()
    # time.sleep(2)
    # checkboxbtn = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    # checkboxbtn.click()
    # submitbtn = driver.find_element(By.XPATH, "//span[text()='Submit']")
    # submitbtn.click()
    # confirmationbtn = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//div[text()='Yes']")))
    # confirmationbtn.click()
    # time.sleep(15)

    driver.quit()
