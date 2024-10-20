# Selenium E-commerce Automation Project

## Overview

This project automates a series of test cases for a dummy e-commerce website [SauceDemo](https://www.saucedemo.com/) using Selenium WebDriver in Python. The tasks involve automating basic actions such as navigation, login, adding items to the cart, checkout, and logout.

## Features

1. *Imports*: Required modules are imported, such as Selenium WebDriver to control the browser, time to add delays, and Keys for simulating keyboard input.
2. *initialize_driver*: This function starts the Chrome browser and maximizes the window.
3. *navigate_to_site*: Opens the SauceDemo website and waits for 2 seconds to ensure the page loads.
4. *login*: Fills in the login form with username and password, then clicks the login button. It waits for a couple of seconds for page transitions.
5. *test_navigate_to_homepage*: Verifies the homepage by checking the page title after navigation.
6. *test_login_functionality*: Checks both valid and invalid login functionality. For invalid login, it ensures that an error message appears.
7. *test_add_items_to_cart*: Logs in, adds two items to the cart, and verifies that the cart has exactly two items.
8. *test_checkout_process*: Adds items to the cart, proceeds to checkout, enters user details, and verifies the total price before completing the checkout process.
9. *test_logout*: Logs in and then logs out by clicking the sidebar menu's logout link. Finally, it checks if the user is redirected back to the login page.

## Technologies Used

- *Python*: Scripting language for writing the tests.
- *Selenium WebDriver*: Used for automating browser interactions.
- *Chrome WebDriver*: A browser driver for Chrome (can be replaced with Firefox or another browser).

## Prerequisites

1. *Python* should be installed on your machine. You can download Python from the [official website](https://www.python.org/).
2. *Selenium* package can be installed via pip:
   ```bash
   pip install selenium
   
