import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

LOGIN_URL = "https://bfdev.tsbcloud.in/"

CHROME_DRIVER_PATH = '/usr/bin/chromedriver'  # Replace with your actual chromedriver path
LOGIN_URL = "https://bfdev.tsbcloud.in/"  # Django login URL

chrome_options = Options()
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to log in with specific credentials using XPath
def login(username, password):
    try:
        # Navigate to the login page
        driver.get(LOGIN_URL)
        
        # Locate username and password fields using XPath and input credentials
        username_field = driver.find_element(By.XPATH, '//*[@id="username"]')
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')

        # Enter credentials from parameters
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)

        # Submit the form
        password_field.send_keys(Keys.RETURN)

        # Check if login is successful by locating a unique element on the post-login page
        driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to load
        # Locate the element using XPath and perform the click
        time.sleep(2)
        #logout button
        profile_element = driver.find_element("xpath",'//*[@id="page-header-user-dropdown"]/span')
        profile_element.click()
        element = driver.find_element("xpath", '//*[@id="page-topbar"]/div/div[3]/div/div/a')
        element.click()
        print(f"Login successful for user: {username}") 
    except TimeoutException:
        print(f"Login failed for user: {username}")
    finally:
        # Attempt to locate and click the logout button if login was successful
        try:
            logout_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/button[@id="logout_button"]'))  # Adjust XPath for logout
            )
            logout_button.click()
            print(f"Logged out user: {username}")
        except TimeoutException:
            print(f"Could not log out user: {username}")

# Function to read users from CSV and test login for each user
def run_multiple_logins():
    with open('/home/dell/test/test_env/users.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['username']
            password = row['password']
            print(f"Attempting login for {username}...")
            login(username, password)
            # Wait between logins

# Execute the test
try:
    run_multiple_logins()
finally:
    driver.quit()
    print("Test completed and browser closed.")