import time
import csv
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Appium options
options = AppiumOptions()
options.load_capabilities({
    "appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "ZD222D4VHB",
    "appium:appPackage": "org.mahiti.stagingpragati",
    "appium:appWaitActivity": "org.cry.pragati.Splash",
    "appium:appWaitActivity": "*",
    "appium:appWaitDuration": 30000,
    "appium:app": "/home/dell/Downloads/cry-staging-24.3.1.2(103)-22-11-2024.apk",
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

# Path to the CSV file containing user credentials
csv_file_path = "/home/dell/test/test_env/cry_user.csv"  # Update with the correct path

# Initialize the Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    with open(csv_file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            username = row["username"]
            password = row["password"]

            print(f"Logging in with username: {username}")

            try:
                # Enter username
                username_field = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/edtUserName"))
                )
                username_field.clear()
                username_field.send_keys(username)

                # Enter password
                password_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/edtPassword"))
                )
                password_field.clear()
                password_field.send_keys(password)

                # Click login button
                login_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/btnLogin"))
                )
                login_button.click()

                print("Login successful. Checking for zip file...")

                try:
                    # Check if zip file alert is present
                    zip_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((AppiumBy.ID, "android:id/button1"))
                    )
                    zip_button.click()
                    print("Zip file is not available. Logging out...")

                    # Logout if zip file is not available
                    logout_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/logout"))
                    )
                    logout_button.click()

                    confirm_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((AppiumBy.ID, "android:id/button1"))
                    )
                    confirm_button.click()
                    print("Logout successful. Proceeding to the next user.")
                    continue
                except TimeoutException:
                    print("Zip file is present. Proceeding to content update page...")

                # Wait for content update to complete
                WebDriverWait(driver, 600).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.LinearLayout\").instance(4)"))
                )
                print("Content update completed.")

                # Logout process after content update
                print("Logging out...")
                logout_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/logout"))
                )
                logout_button.click()

                confirm_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, "android:id/button1"))
                )
                confirm_button.click()
                print("Logout successful. Proceeding to the next user.")

            except (TimeoutException, NoSuchElementException) as e:
                print(f"Error during login/logout for user {username}: {e}")

finally:
    driver.quit()
    print("Test completed.")
