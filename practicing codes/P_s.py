from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://google.com")

input_element= driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("facebook"+ Keys.ENTER)
time.sleep(7)
driver.quit()