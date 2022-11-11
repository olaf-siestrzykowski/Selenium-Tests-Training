import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += r'C:/Selenium_driver'
driver = webdriver.Chrome()

'''driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
driver.implicitly_wait(8)
element = driver.find_element(By.ID, 'downloadButton')
element.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), 'Complete!'
    )
)'''

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
driver.implicitly_wait(4)
num1 = driver.find_element(By.ID, 'sum1')
num2 = driver.find_element(By.ID, 'sum2')

try:
    no_button = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    no_button.click()
except:
    print('No button with that class name.')

num1.send_keys(Keys.NUMPAD4, Keys.NUMPAD5)
num2.send_keys(Keys.NUMPAD6, Keys.NUMPAD9)
btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btn.click()
