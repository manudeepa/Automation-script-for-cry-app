from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL for your login page
LOGIN_URL = 'https://bfdev.tsbcloud.in/'  # Replace with your actual login URL

# User credentials
USERNAME = 'chetan_nandha'  # Replace with the actual username
PASSWORD = 'Data@123'  # Replace with the actual password

# Set up Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Function to perform login
def login(username, password):
    try:
        # Navigate to the login page
        driver.get("https://bfdev.tsbcloud.in/")

        # Wait until the username field is visible and clickable
        username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="id_username"]'))  # Adjust XPath based on your app's HTML structure
        )
        username_field.clear()  # Clear any pre-filled text
        username_field.send_keys(username)  # Enter the username

        # Locate the password field and input the password
        password_field = driver.find_element(By.XPATH, '//*[@id="id_password"]')  # Adjust XPath based on your app's HTML structure
        password_field.clear()  # Clear any pre-filled text
        password_field.send_keys(password)  # Enter the password

        # Submit the form (press Enter on the password field)
        password_field.send_keys(Keys.RETURN)

        # Wait for the page to load and verify successful login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Welcome")]'))  # Adjust XPath to match a unique element post-login
        )

        print(f"Login successful for {username}!")

    except Exception as e:
        print(f"Error during login for {username}: {e}")
    finally:
        # Wait for a few seconds to observe the result
        time.sleep(5)

# Execute the login function for the single user
login(USERNAME, PASSWORD)

# Close the browser after the process is complete
driver.quit()
