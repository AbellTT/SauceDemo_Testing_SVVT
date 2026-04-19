import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def driver():
    """
    This is a Pytest Fixture!
    It automatically runs BEFORE every single test function to open Chrome.
    Then it yields control to the test.
    Once the test is done, it runs the code AFTER the yield to close Chrome.
    """
    print("\n[SETUP] Initializing Chrome Browser...")
    # Initialize Chrome
    driver = webdriver.Chrome()
    # Maximize window and set a global implicit wait for elements to load
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Give the driver to the test function
    yield driver
    # After the test finishes (or if it crashes), close the browser!
    print("\n[TEARDOWN] Closing Browser...")
    time.sleep(1)
    driver.quit()
