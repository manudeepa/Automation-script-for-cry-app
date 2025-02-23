import csv
import time
import pandas as pd
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Appium Desired Capabilities
options = AppiumOptions()
options.load_capabilities({
    "appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:platformVersion": "15",
    "appium:deviceName": "00078344R000676",
    "appium:appWaitActivity": "*",
    "appium:appWaitDuration": 30000,
    "appium:app": "/home/dell/Downloads/cry-staging-24.3.1.2(103)-22-11-2024.apk",
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

# Initialize Appium driver
def initialize_driver():
    return webdriver.Remote("http://127.0.0.1:4723", options=options)

driver = initialize_driver()

# File paths
input_csv = "/home/dell/test/test_env/cry_user.csv"  # Contains username and password
output_csv = "login_validation_results.csv"

# Function to read users from a CSV file
def read_users_from_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]

# Function to write validation results to a CSV file
def write_validation_to_csv(results, file_path):
    df = pd.DataFrame(results)
    df.to_csv(file_path, index=False)

# Function to clear cache
def clear_cache():
    try:
        print("Clearing cache of the previous user...")
        clear_cache_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))
        )
        clear_cache_button.click()
        print("Cache cleared successfully.")
    except TimeoutException:
        print("Clear cache failed: Clear cache button not found.")

# Function to check zip file availability
def check_zip_file():
    # import ipdb;ipdb.set_trace()
    zip_present=True
    try:
        zip_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))
        )
        # 00000000-0000-02ed-ffff-ffff00000098
        if zip_button.id == '00000000-0000-02ed-ffff-ffff00000098':
            print("Zip file is not available. App automatically logged out.")
            zip_present =  False  # Indicates that no further action is needed
        else: 
          print("No zip file alert present. Proceeding with content update.")
          zip_present =  True  # Indicates to proceed with content update
        zip_button.click()  # Dismiss zip file alert
    except TimeoutException:
        print("No zip file alert present. Proceeding with content update.")
        zip_present =  True  # Indicates to proceed with content update

    return zip_present

# def check_zip_file():
#     import ipdb;ipdb.set_trace()
#     try:
#         zip_button = WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))
#         )
#         zip_button.click()  # Dismiss zip file alert
#         print("Zip file is not available. App automatically logged out.")
#         return False  # Indicates that no further action is needed
#     except TimeoutException:
#         print("No zip file alert present. Proceeding with content update.")
#         return True  # Indicates to proceed with content update

# Function to perform content update
def content_update():
    print("Starting content update...")
    try:
        WebDriverWait(driver, 110).until(
            EC.presence_of_element_located((AppiumBy.ID, 'org.mahiti.stagingpragati:id/location_status'))
        )
        WebDriverWait(driver, 110).until(
            EC.presence_of_element_located((AppiumBy.ID, 'org.mahiti.stagingpragati:id/beneficiary_status'))
        )
        WebDriverWait(driver, 110).until(
            EC.presence_of_element_located((AppiumBy.ID, 'org.mahiti.stagingpragati:id/datacollection_progressbar'))
        )
        WebDriverWait(driver, 110).until(
            EC.presence_of_element_located((AppiumBy.ID, 'org.mahiti.stagingpragati:id/other_progressbar'))
        )
        print("Content update completed.")
    except TimeoutException:
        print("Content update failed: Timeout occurred.")

# Function to perform logout
def logout():
    try:
        print("Logging out...")
        logout_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/logout"))
        )
        logout_button.click()
        confirm_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, "android:id/button1"))
        )
        confirm_button.click()
        print("Logout successful.")
    except TimeoutException:
        print("Logout failed: Logout button not found.")

# Function to login and validate user
def login_and_validate(user):
    username = user['username']
    password = user['password']
    validation_message = ""
    zip_file_present = True

    try:
        # Wait for username and password fields
        username_field = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/edtUserName"))
        )
        password_field = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/edtPassword"))
        )
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((AppiumBy.ID, "org.mahiti.stagingpragati:id/btnLogin"))
        )

        # Input credentials and click login
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()

        # Check zip file availability
        zip_file_present = check_zip_file()
        if not zip_file_present:
            validation_message = "No zip file. Logged out immediately."
            logout()
            return {
                "username": username,
                "validation_message": validation_message,
                "zip_file_present": zip_file_present
            }  # Exit early if no zip file

        # If zip file is present, proceed with clearing cache and content update
        clear_cache()
        content_update()
        time.sleep(450)  # Wait for content update to complete
        logout()
        validation_message = "Content update completed and logged out."

    except TimeoutException as e:
        validation_message = f"Error during login: Timeout occurred. {str(e)}"
    except NoSuchElementException as e:
        validation_message = f"Error during login: Element not found. {str(e)}"

    return {
        "username": username,
        "validation_message": validation_message,
        "zip_file_present": zip_file_present
    }

# Main function
def main():
    users = read_users_from_csv(input_csv)
    validation_results = []

    for index, user in enumerate(users):
        print(f"Processing user {user['username']} ({index + 1}/{len(users)})...")
        result = login_and_validate(user)
        validation_results.append(result)

        # Adjust delay based on zip file presence
        if result["zip_file_present"]:
            print("Waiting for 450 seconds before processing the next user.")
            # time.sleep(450)
        else:
            print("Waiting for 10 seconds before processing the next user.")
            time.sleep(10)

    # Write validation results to CSV
    write_validation_to_csv(validation_results, output_csv)
    print(f"Validation results written to {output_csv}")

    driver.quit()

if __name__ == "__main__":
    main()