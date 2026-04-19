from selenium import webdriver
import time

# In Pytest, your functions MUST start with the word "test_"
def test_orangehrm_login_page_title():
    print("\n--- Starting Pytest Practice ---")
    # 1. SETUP: Open the browser
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    # Let it load for a second
    time.sleep(3)
    # 2. ACTION: Get the actual title of the webpage
    actual_title = driver.title
    expected_title = "OrangeHRM"
    print(f"The website title is: {actual_title}")
    # 3. ASSERTION: This is the magic of Pytest!
    # Instead of writing "if/else" statements, you just use "assert".
    # If the statement is True, the test PASSES. If False, the test FAILS.
    assert actual_title == expected_title, f"Error: Title was {actual_title}, but we expected {expected_title}"
    # 4. TEARDOWN: Close the browser
    driver.quit()
    print("--- Test Passed and Browser Closed ---")
# Let's add a second test that we intentionally force to fail so you can see what it looks like!
def test_intentional_failure_example():
    # We assert that 2 + 2 equals 5. This will fail!
    assert 2 + 2 == 5, "Math is broken!"
