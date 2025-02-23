from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Desired capabilities for Appium to connect to a mobile device
desired_caps = {
    "platformName": "Android",  # "iOS" for iOS devices
    "platformVersion": "14",  # Specify the Android version you're testing on
    "deviceName": "Nothing Phone (2a)",  # The name of your Android device/emulator
    "appPackage": "org.thesocialbytes.bajajfd",  # Replace with your app's package name
    "appActivity": "com.example.app.MainActivity",  # Replace with your app's main activity
    "noReset": True,  # Prevents app reset between sessions
    "automationName": "UiAutomator2",  # Use UiAutomator2 for Android
}

# Connect to the Appium server (assuming it's running on localhost)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# Wait for the app to load (you can replace this with WebDriverWait)
sleep(5)  # Wait for 5 seconds for the app to load, adjust this as necessary

# Find the username, password fields, and login button
username_field = driver.find_element(By.ID, "com.example.app:id/username")  # Replace with actual username field ID
password_field = driver.find_element(By.ID, "com.example.app:id/password")  # Replace with actual password field ID
login_button = driver.find_element(By.ID, "com.example.app:id/login_button")  # Replace with actual login button ID

# Enter login credentials
username_field.send_keys("your_username")  # Replace with the actual username
password_field.send_keys("your_password")  # Replace with the actual password

# Click the login button
login_button.click()

# Wait for login to complete and verify the login success
sleep(5)  # Wait for the login action to complete, adjust this as necessary

# Check for a successful login by looking for an element that appears post-login
try:
    # For example, check if a profile icon appears after login
    profile_icon = driver.find_element(By.ID, "com.example.app:id/profile_icon")  # Replace with actual element ID
    print("Login successful!")
except:
    print("Login failed!")

# Close the app and end the session
driver.quit()
