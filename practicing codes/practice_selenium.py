from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Starting Selenium Practice Test with Google Chrome...")
driver = webdriver.Chrome()

try:
    print("Opening OrangeHRM...")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    print("Waiting for login form...")
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.TAG_NAME, "button")
    print("Typing credentials...")
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")    
    print("Clicking login button...")
    login_button.click()
    time.sleep(5)
    print("Practice test completed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Closing browser...")
    driver.quit()
