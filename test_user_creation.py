from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv
import time
from selenium.common.exceptions import ElementClickInterceptedException

# Setup Selenium WebDriver
CHROME_DRIVER_PATH = '/usr/bin/chromedriver'  # Replace with your actual chromedriver path
LOGIN_URL = "https://bfdev.tsbcloud.in/"  # Django login URL

chrome_options = Options()
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 30)  # Set the timeout for wait (in seconds)

# Define URLs and credentials
login_url = "https://bfdev.tsbcloud.in/"  # replace with actual login URL
username = "admin"                   # replace with actual username
password = "admin@2023"               # replace with actual password

# Error log list
validation_errors = []

# Step 1: Login
def login():
    driver.get(login_url)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))).send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/div[2]/form/div[4]/button').click()

# Step 2: Navigate to Configuration > User Menu
def navigate_to_user_menu():
    configuration_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="side-menu"]/li[2]/a')))
    configuration_menu.click()

    user_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[1]/a/span')))
    user_menu.click()

# Step 3: Click on Add User button
def open_add_user_form():
    add_user_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/div[3]/a[1]/button/em')))
    add_user_button.click()

# Step 4: Create User with CSV Data
def create_user(user_data):
    try:
        # Fill in the user creation form
        driver.find_element(By.XPATH, '//*[@id="id_first_name"]').send_keys(user_data['first_name'])
        driver.find_element(By.XPATH, '//*[@id="id_last_name"]').send_keys(user_data['last_name'])
        driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys(user_data['username'])
        driver.find_element(By.XPATH, '//*[@id="id_email"]').send_keys(user_data['email'])
        driver.find_element(By.XPATH, '//*[@id="id_mobile_number"]').send_keys(user_data['mobile'])
        driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys(user_data['password'])
        driver.find_element(By.XPATH, '//*[@id="id_confirm_password"]').send_keys(user_data['confirm_password'])
        driver.find_element(By.XPATH, '//*[@id="id_organization_unit"]').send_keys(user_data['organization_unit'])
        driver.find_element(By.XPATH, '//*[@id="id_role_type"]').send_keys(user_data['roles'])
        
        
        # Submit the form    
        user_save = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/form/div[2]/div/button')))
        time.sleep(0.5)  # Small delay to let the scroll finish
        user_save.click()


        # Confirm the user creation or catch any error message
        try:
            success_message = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="RegisterValidation"]/div[2]/div/button')))
            print(f"{user_data['username']} created successfully!")
            return True
        except:
            error_message = driver.find_element(By.XPATH, '//*[@id="RegisterValidation"]/div[1]/div[3]/div[1]/div/ul/li/text()').text
            print(f"Failed to create user {user_data['username']}: {error_message}")
            validation_errors.append([user_data['username'], user_data['email'], error_message])
            return False

    except Exception as e:
        print(f"Error creating user {user_data['username']}: {e}")
        validation_errors.append([user_data['username'], user_data['email'], str(e)])
        return False

# Save validation errors to a CSV
def save_validation_errors(errors, filename='validation_errors.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User Name", "Email","Error Message"])
        writer.writerows(errors)

# Load CSV and process each user
def create_users_from_csv(file_path):
    with open(file_path, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            # Validation checks
            if row['password'] != row['confirm_password']:
                error_message = f"Password mismatch for user {row['username']}"
                print(error_message)
                validation_errors.append([row['username'], row['email'], error_message])
                continue

            if not all(row[key] for key in ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']):
                error_message = f"Missing required fields for user {row['username']}"
                print(error_message)
                validation_errors.append([row['username'], row['email'], error_message])
                continue

            # Open add user form and create the user
            open_add_user_form()
            user_created = create_user(row)

            # If the user was created, go back to the user list for the next user
            if user_created:
                navigate_to_user_menu()
                time.sleep(1)

# Run the script
try:
    login()
    navigate_to_user_menu()
    create_users_from_csv("/home/dell/test/test_env/user_list.csv")
finally:
    # Save validation errors after completion
    if validation_errors:
        save_validation_errors(validation_errors, 'validation_errors.csv')
    driver.quit()



