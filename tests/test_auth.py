from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Typing Effect Helper ---
def slow_type(element, text, delay=0.25):
    """Types characters one by one with a delay to simulate human typing!"""
    for character in text:
        element.send_keys(character)
        time.sleep(delay)

# --- Helper Function ---
def login_helper(driver, username, password):
    """Helper function so we don't rewrite the login steps in every test"""
    driver.get("https://opensource-demo.orangehrmlive.com/")
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = driver.find_element(By.NAME, "password")
    slow_type(username_field, username)
    slow_type(password_field, password)
    driver.find_element(By.TAG_NAME, "button").click()

def logout_helper(driver):
    """Helper function to handle the dropdown animation when logging out"""
    wait = WebDriverWait(driver, 10)
    
    # Click profile dropdown
    profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab")))
    profile_icon.click()
    
    # OrangeHRM has a slide-down CSS animation. We must pause to let it finish!
    time.sleep(1)
    
    # Click Logout
    logout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
    logout_button.click()

# --- TC_001: Valid Login ---
def test_valid_login(driver):
    login_helper(driver, "Admin", "admin123")
    # Assert we reached the dashboard by checking the URL
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url, "Login failed: Did not reach dashboard!"

# --- TC_002: Invalid Login ---
def test_invalid_login(driver):
    login_helper(driver, "Admin", "wrongpassword")
    # Wait for the specific error message popup
    wait = WebDriverWait(driver, 10)
    # Selenium Rule: You cannot use By.CLASS_NAME with spaces! You must use CSS_SELECTOR with dots.
    error_msg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-text.oxd-text--p.oxd-alert-content-text")))
    assert error_msg.text == "Invalid credentials", f"Expected 'Invalid credentials', but got '{error_msg.text}'"

# --- TC_003: Logout ---
def test_logout(driver):
    # Log in first
    login_helper(driver, "Admin", "admin123")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("dashboard"))

    # Use our new helper to safely click the logout button!
    logout_helper(driver)
    
    # Assert we are back on the login page
    wait.until(EC.url_contains("login"))
    assert "login" in driver.current_url, "Logout failed: Not on login page!"

# --- TC_004: Session Security ---
def test_session_security_back_button(driver):
    # Log in first, just like TC_003
    login_helper(driver, "Admin", "admin123")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("dashboard"))
    
    # Suite Stabilization: Let the dashboard fully register in the browser history
    time.sleep(2)

    # Run the logout flow safely using the helper, NOT the test!
    logout_helper(driver)
    
    # Suite Stabilization: Let the login page fully register in the browser history
    wait.until(EC.url_contains("login"))
    time.sleep(2)
    
    # Try to press the back button to bypass security!
    driver.back()
    
    # Assert we are still blocked and forced to stay on the login page
    # OrangeHRM uses Javascript to redirect unauthorized users. 
    # Checking if the login form is present is safer than checking the URL string!
    try:
        wait.until(EC.presence_of_element_located((By.NAME, "username")))
    except:
        assert False, "Security flaw: Back button restored the dashboard without redirecting to login!"
