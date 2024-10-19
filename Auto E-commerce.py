from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to initialize the Chrome WebDriver
def initialize_driver():
    driver = webdriver.Chrome()  # Initializes Chrome WebDriver
    driver.maximize_window()  # Maximize the browser window
    return driver  # Returns the driver object

# Function to navigate to the SauceDemo website
def navigate_to_site(driver):
    driver.get("https://www.saucedemo.com/")  # Opens the SauceDemo URL

# Function to log in with specified credentials
def login(driver, username, password):
    wait_for_element(driver, By.ID, "user-name").send_keys(username)
    wait_for_element(driver, By.ID, "password").send_keys(password)
    wait_for_element(driver, By.ID, "login-button").click()

# Function to wait for an element to be visible
def wait_for_element(driver, by, value):
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))

# Task 1: Launch the browser and navigate to the homepage
def test_navigate_to_homepage():
    driver = initialize_driver()
    navigate_to_site(driver)

    # Validate the page title to ensure it's correct
    assert "Swag Labs" in driver.title, f"Expected 'Swag Labs' in title, got '{driver.title}'"
    print("Page title verified.")

    driver.quit()

# Task 2: Login with both valid and invalid credentials
def test_login_functionality():
    driver = initialize_driver()
    navigate_to_site(driver)

    # Test valid credentials
    print("Testing valid login...")
    login(driver, "standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url, f"Expected 'inventory.html' in URL, got {driver.current_url}"
    print("Valid login successful.")

    # Test invalid credentials
    driver.get("https://www.saucedemo.com/")
    print("Testing invalid login...")
    login(driver, "invalid_user", "invalid_pass")
    error_message = wait_for_element(driver, By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_message, f"Expected 'Epic sadface' in error message, got '{error_message}'"
    print("Invalid login test passed.")

    driver.quit()

# Task 3: Add items to the cart
def test_add_items_to_cart():
    driver = initialize_driver()
    navigate_to_site(driver)
    login(driver, "standard_user", "secret_sauce")

    # Add items to the cart
    print("Adding items to the cart...")
    wait_for_element(driver, By.ID, "add-to-cart-sauce-labs-backpack").click()
    wait_for_element(driver, By.ID, "add-to-cart-sauce-labs-bike-light").click()

    # Verify the cart has the correct number of items
    cart_count = wait_for_element(driver, By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "2", f"Expected 2 items in cart, got {cart_count}"
    print(f"Added {cart_count} items to the cart successfully.")

    driver.quit()

# Task 4: Checkout process
def test_checkout_process():
    driver = initialize_driver()
    navigate_to_site(driver)
    login(driver, "standard_user", "secret_sauce")

    # Add items to the cart
    wait_for_element(driver, By.ID, "add-to-cart-sauce-labs-backpack").click()
    wait_for_element(driver, By.ID, "add-to-cart-sauce-labs-bike-light").click()

    # Proceed to checkout
    print("Proceeding to checkout...")
    wait_for_element(driver, By.CLASS_NAME, "shopping_cart_link").click()
    wait_for_element(driver, By.ID, "checkout").click()

    # Enter user details for checkout
    wait_for_element(driver, By.ID, "first-name").send_keys("Isha")
    wait_for_element(driver, By.ID, "last-name").send_keys("Soni")
    wait_for_element(driver, By.ID, "postal-code").send_keys("560037")
    wait_for_element(driver, By.ID, "continue").click()

    # Validate total price displayed during checkout
    total_price = wait_for_element(driver, By.CLASS_NAME, "summary_total_label").text
    assert "$" in total_price, f"Expected total price to contain '$', got '{total_price}'"
    print(f"Total price: {total_price}")

    # Complete the checkout process
    wait_for_element(driver, By.ID, "finish").click()

    # Confirm the order completion
    confirmation_message = wait_for_element(driver, By.CLASS_NAME, "complete-header").text
    assert "thank you for your order" in confirmation_message.lower(), f"Expected confirmation message to contain 'thank you for your order', got '{confirmation_message}'"

    print("Checkout completed successfully.")

    driver.quit()

# Task 5: Logout functionality
def test_logout():
    driver = initialize_driver()
    navigate_to_site(driver)
    login(driver, "standard_user", "secret_sauce")

    # Start the logout process
    wait_for_element(driver, By.ID, "react-burger-menu-btn").click()
    wait_for_element(driver, By.ID, "logout_sidebar_link").click()

    # Verify that the user is back on the login page
    assert "https://www.saucedemo.com/" in driver.current_url, f"Expected URL to be 'https://www.saucedemo.com/', got '{driver.current_url}'"
    print("Logout successful. Back to the login page.")

    driver.quit()

# Main function to execute all the test cases sequentially
if __name__ == "__main__":
    test_navigate_to_homepage()
    test_login_functionality()
    test_add_items_to_cart()
    test_checkout_process()
    test_logout()