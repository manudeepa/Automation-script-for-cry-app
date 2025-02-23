from os import wait
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


options = AppiumOptions()
options.load_capabilities({
	"appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "ZD222D4VHB",
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


try:
    # Login sequence
    username = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/edtUserName")))
    username.send_keys("rwds3")
    password = driver.find_element(by=AppiumBy.ID, value="org.mahiti.stagingpragati:id/edtPassword")
    password.send_keys("cry@2018")
    submit_button = driver.find_element(by=AppiumBy.ID, value="org.mahiti.stagingpragati:id/btnLogin")
    submit_button.click()
    username = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/edtUserName")))
    username.send_keys("rwds3")
    password = driver.find_element(by=AppiumBy.ID, value="org.mahiti.stagingpragati:id/edtPassword")
    password.send_keys("cry@2018")
    submit_button = driver.find_element(by=AppiumBy.ID, value="org.mahiti.stagingpragati:id/btnLogin")
    submit_button.click()

    # Wait for the target element and interact
    el1 = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.LinearLayout\").instance(4)")
        )
    )
    el1.click()

    # Logout
    logout_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
    logout_button.click()

except TimeoutException:
    print("Element not found within the time limit. Please check the locator or wait settings.")

finally:
    driver.quit()