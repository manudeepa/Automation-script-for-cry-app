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

LOGIN_URL = "https://bfdev.tsbcloud.in/"  # Django login URL

CHROME_DRIVER_PATH = '/usr/bin/chromedriver'  # Replace with your actual chromedriver path

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

        # # Check if login is successful by locating a unique element on the post-login page
        # driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to load
        # time.sleep(2)
        
        # # Logout button (just to ensure that login was successful)
        # profile_element = driver.find_element("xpath",'//*[@id="page-header-user-dropdown"]/span')
        # profile_element.click()
        # element = driver.find_element("xpath", '//*[@id="page-topbar"]/div/div[3]/div/div/a')
        # element.click()
        # print(f"Login successful for user: {username}")
        
        # Add the Export report logic after successful login
        export_report()

    except TimeoutException:
        print(f"Login failed for user: {username}")

# Function to handle the Export Report process
# Function to handle the Export Report process
from selenium.webdriver.common.action_chains import ActionChains

# Function to handle the Export Report process
def export_report():
    try:
        # Close any potential popups or dropdown menus that might block the 'Download' button
        close_dropdown_if_present()

        # Wait for the 'Export reports' option to be clickable and click on it
        export_reports_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Export reports')]"))
        )
        export_reports_button.click()
        time.sleep(3)

        # Click the 'Export CSV' option
        export_csv_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/reports/exportcsv/export-reports/']"))
        )
        export_csv_button.click()
        time.sleep(3)

        # Scroll the 'Download' button into view and click it
        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="datatables"]/tbody/tr[9]/td[5]/a'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", download_button)
        time.sleep(0.5)  # Small delay to ensure scroll completes

        # Optional: Use ActionChains to click to bypass any possible issue with the click interception
        ActionChains(driver).move_to_element(download_button).click().perform()

        print("Export report and download initiated.")

    except TimeoutException:
        print("Failed to initiate the report export or download.")

# Function to close any dropdown or header menu that might be blocking the download button
def close_dropdown_if_present():
    try:
        # Try to close the user profile dropdown if open (based on observed error message)
        dropdown_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "page-header-user-dropdown"))
        )
        dropdown_button.click()  # Close the dropdown by clicking it
        print("Closed the user dropdown.")
    except TimeoutException:
        print("No dropdown menu found to close.")


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
