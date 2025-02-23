from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv
import time
import re  # For regex validation
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

# Setup Selenium WebDriver
CHROME_DRIVER_PATH = '/usr/bin/chromedriver'  # Replace with your actual chromedriver path
LOGIN_URL = "https://bfdev.tsbcloud.in/"  # Django login URL

chrome_options = Options()
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 30)  # Set the timeout for wait (in seconds)

# Define URLs and credentials
login_url = "https://bfdev.tsbcloud.in/"  # replace with actual login URL
username = "admin"  # replace with actual username
password = "admin@2023"  # replace with actual password

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
    try:
        add_user_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/div[3]/a[1]/button/em')))
        time.sleep(1)
        add_user_button.click()
    except TimeoutException:
        error_message = "Timeout: Add User button not found within the given time."
        print(error_message)
        validation_errors.append([None, None, error_message])
        return False
    except Exception as e:
        print("Error clicking Add User button:" +str(e))
        validation_errors.append([None, None, str(e)])
        return False
    return True

# Validate Email Format
def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

# Validate Mobile Number
def is_valid_mobile(mobile):
    return mobile.isdigit() and 9 <= len(mobile) <= 11

# Validate Password (6-10 characters, 1 capital, 1 lowercase, 1 number, 1 special character)
def is_valid_password(password):
    if len(password) < 6 or len(password) > 10:
        return False
    if not re.search(r'[A-Z]', password):  # Check for at least one capital letter
        return False
    if not re.search(r'[a-z]', password):  # Check for at least one lowercase letter
        return False
    if not re.search(r'[0-9]', password):  # Check for at least one number
        return False
    if not re.search(r'[@#$]', password):  # Check for at least one special character
        return False
    return True

# Check for Duplicate Username or Email
def is_duplicate_user(user_data, processed_users):
    return user_data['username'] in processed_users['usernames'] or user_data['email'] in processed_users['emails']

# Step 4: Create User with CSV Data
def create_user(user_data, processed_users):
    try:
        # Validate password before proceeding
        if not is_valid_password(user_data['password']):
            error_message = "Password must be between 6 to 10 characters long and contain 1 capital letter, 1 lowercase letter, 1 number, and 1 special character (@#$). eg: Jamesbond@123 for user {user_data['username']}"
            print(error_message)
            validation_errors.append([user_data['username'], user_data['email'], error_message])
            return False

        # Validate fields before submission
        if not is_valid_email(user_data['email']):
            error_message = "Invalid email format for user {user_data['username']}"
            print(error_message)
            validation_errors.append([user_data['username'], user_data['email'], error_message])
            return False

        if not is_valid_mobile(user_data['mobile']):
            error_message = f"Invalid mobile number for user {user_data['username']}"
            print(error_message)
            validation_errors.append([user_data['username'], user_data['email'], error_message])
            return False

        if not all([user_data['organization_unit'], user_data['roles']]):
            error_message = f"Mandatory dropdown values missing for user {user_data['username']}"
            print(error_message)
            validation_errors.append([user_data['username'], user_data['email'], error_message])
            return False

        if is_duplicate_user(user_data, processed_users):
            error_message = f"Duplicate username or email for user {user_data['username']}"
            print(error_message)
            validation_errors.append([user_data['username'], user_data['email'], error_message])
            return False

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
            success_message = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/comment()[27]')))
            print(f"{user_data['username']} created successfully!")
            processed_users['usernames'].add(user_data['username'])
            processed_users['emails'].add(user_data['email'])
            return True
        except:
            error_message = driver.find_element(By.XPATH, '//*[@id="RegisterValidation"]/div[1]/div[2]/div[1]/div/div/ul/li').click
            error_message = driver.find_element(By.XPATH, '//*[@id="RegisterValidation"]/div[1]/div[3]/div[1]/div/ul/li/text()').click
            error_message = driver.find_element(By.XPATH, '//*[@id="id_mobile_number-error"]').click
            # error_message = driver.find_element(By.XPATH, '//*[@id="RegisterValidation"]/div[1]/div[3]/div[1]/div/ul/li/text()').click
            error_message = driver.find_element(By.XPATH, '//*[@id="RegisterValidation"]/div[1]/div[3]/div[2]/div/div/ul/li').click
            error_message = driver.find_element(By.XPATH, '//*[@id="RegisterValidation"]/div[1]/div[3]/div[2]/div/div/ul/li/text()').click
            error_message = driver.find_element(By.XPATH, '//*[@id="RegisterValidation"]/div[1]/div[5]/div/div/div/ul/li').click

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
        writer.writerow(["User Name", "Email", "Error Message"])
        writer.writerows(errors)

# Load CSV and process each user
def create_users_from_csv(file_path):
    processed_users = {'usernames': set(), 'emails': set()}  # Keep track of processed usernames and emails
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
            user_created = create_user(row, processed_users)

             # If the user was created, go back to the user list for the next user
            if user_created:
                navigate_to_user_menu()
                time.sleep(1)
                

# Run the script
try:
    login()
    navigate_to_user_menu()
    create_users_from_csv("/home/dell/test/test_env/user_one.csv")
finally:
    # Save validation errors after completion
    if validation_errors:
        save_validation_errors(validation_errors, 'validation_errors.csv')
    driver.quit()