import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize Appium options
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
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Initialize WebDriverWait with a 10-second timeout
wait = WebDriverWait(driver, 550)

# Login sequence
username = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/edtUserName")))
username.send_keys("rwds3")
print("User Name Entered.....")

password = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/edtPassword")))
password.send_keys("cry@2018")
print("Password Entered.....")

submit_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/btnLogin")))
submit_button.click()
print("User going to login...")

print("Content update going on.....")

pragathi_flow = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/pragati_flow")))
pragathi_flow.click()
print("Going to Pragathi flow.....")
time.sleep(10)

# Replacing 'presence_of_all_elements_located' with 'presence_of_element_located'
save = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/btnSave")))
save.click()
print("Click on save button in Periodicity select page.....")
time.sleep(10)

location_apply = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/btn_apply")))
location_apply.click()
print("Click on apply button in Hamlet select page.....")
time.sleep(10)

home_navigation = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/homeNavigation")))
home_navigation.click()
print("Going to Home Page.....")
time.sleep(10)

days_popup = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
days_popup.click()
time.sleep(10)

household_add = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.mahiti.stagingpragati:id/lblListItem" and @text="Household"]')))
print("Click on Hpuse hold add button .....")
household_add.click()

newhousehold_add = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/createNewButton")))
newhousehold_add.click()
print("Going to hosehold add.....")


consent_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/rbYes")))
consent_button.click()
print("Going to cick consent form Yes button.....")

consent_next_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/btn_next")))
consent_next_button.click()
print("Click on consent form Next button .....")

addAddress = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/addAddress")))
addAddress.click()
print("Going to add Household address .....")

Location_level = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/locationlevel")))
Location_level.click()
print("Click on Location Operator .....")

location_region = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Rural"]')))
location_region.click()
print("Going to add Urban or rural .....")


location_state = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholdstate")))
location_state.click()
print("Click on state field .....")


location_state_value = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Tamil Nadu"]')))
location_state_value.click()
print("Going to add state .....")


housrholddistrict = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholddistrict")))
housrholddistrict.click()
print("Click On district field .....")


housrholddistrict_value = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Ramanathapuram"]')))
housrholddistrict_value.click()
print("Going to add District .....")


housrholdtaluk = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholdtaluk")))
housrholdtaluk.click()
print("Click on Taluk Field .....")


housrholdtaluk_value = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Kadaladi"]')))
housrholdtaluk_value.click()
print("Going to add Taluk .....")


housrholdgrampanchayat = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholdgrampanchayat")))
housrholdgrampanchayat.click()
print("Click on GP Field .....")


housrholdgrampanchayat_values = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Siraikulam"]')))
housrholdgrampanchayat_values.click()
print("Going to add GP .....")


housrholdvillage = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholdvillage")))
housrholdvillage.click()
print("Click on Village Field .....")


housrholdvillage_values = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="S.Kamarajapuram"]')))
housrholdvillage_values.click()
print("Going to add Village .....")


housrholdhamlet = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholdhamlet")))
housrholdhamlet.click()
print("Click on HM Field .....")


housrholdhamlet_values = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="S.Kamarajapuram"]')))
housrholdhamlet_values.click()
print("Going to add HM .....")


no_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/radio_no")))
no_button.click()
print("Going to Click Address Be Validated? Field .....")


address = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/address1")))
address.send_keys("bengalore")
print("Going to add adress .....")


pincode = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/pincode")))
pincode.send_keys("876567")
print("Going to add Pincode .....")


saveDataButton = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/saveDataButton")))
saveDataButton.click()
print("Going to Click Save Button .....")
time.sleep(10)

name = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/name")))
name.send_keys(" joseph maiyaaa")
print("Going to add HH Name .....")


DOB = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/radio_no")))
DOB.click()
print("Going to Click DOB.....")


year = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageYear")))
year.send_keys("34")
year.click()
print("Going to add Year .....")


month = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageMonth")))
month.send_keys("0")
month.click()
print("Going to add Month .....")


gender = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/beneficiarygender")))
gender.click()
print("Going to Click Gender Field .....")


gender_value = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().text("Male")')))
gender_value.click()
print("Going to add Gender .....")


household_save = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/saveData")))
household_save.click()
print("Going to Click Save Button .....")


Datacollection_form_page = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="org.mahiti.stagingpragati:id/linear"])[1]/android.widget.ImageView')))
Datacollection_form_page.click()
print("Going to HH in Listing Page .....")


Details_page = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Details"]')))
Details_page.click()
print("Going to Click Details Page.....")


add_mother = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/addMother")))
add_mother.click()
print("Going to add Mother.....")


# Additional interactions can be added here

driver.quit()
