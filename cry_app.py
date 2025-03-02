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
    "appium:platformVersion": "15",
    "appium:deviceName": "00078344R000676",
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

# days_popup = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
# days_popup.click()
# time.sleep(10)

household_add = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.mahiti.stagingpragati:id/lblListItem" and @text="Household"]')))
household_add.click()
print("Click on HouseHold add button .....")

newhousehold_add = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/createNewButton")))
newhousehold_add.click()
print("Going to Hosehold add.....")

# Scroll to Consent Form Yes button
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/rbYes"))')
print("Scrolled down to Consent Form Yes button...")

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

# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/address1"))')
print("Scrolled down to Consent Form Yes button...")

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
name.send_keys("Kiran raj Puttur")
print("Going to add HH Name .....")


DOB = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/radio_no")))
DOB.click()
print("Going to Click DOB.....")


# # scroll down
# driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/ageYear"))')
# print("Scrolled down to Consent Form Yes button...")

year = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageYear")))
year.send_keys("34")
year.click()
print("Going to add Year .....")


month = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageMonth")))
month.send_keys("0")
month.click()
print("Going to add Month .....")

# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("android:id/text1"))')
print("Scrolled down to Consent Form Yes button...")

# Locate the gender dropdown and click to open it
gender_dropdown = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/text1")))
gender_dropdown.click()
print("Opened Gender dropdown...")

# Select the 'Male' option using Android UIAutomator
gender_male_option = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Male")')))
gender_male_option.click()
print("Selected 'Male' as gender...")

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


add_mother = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/motherStatusSpinner")))
add_mother.click()
print("Going to add Mother.....")

add_mother_status = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Pregnant"]')))
add_mother_status.click()
print("Going to select mother status.....")

mother_name = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/name")))
mother_name.send_keys("janani puttur")
print("Going to add Mother name.....")

# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/radio_no"))')
print("Scrolled down to Consent Form Yes button...")

mother_dob = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/radio_no")))
mother_dob.click()
print("Going to select Moher Date of birth.....")

mother_year = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageYear")))
mother_year.send_keys(45)
mother_year.click()
print("Going to add Year.....")

mother_month = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageMonth")))
mother_month.send_keys(1)
mother_month.click()
print("Going to add month.....")

mother_save = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/saveData")))
mother_save.click()
print("Going to add Mother.....")

add_child = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/addChild")))
add_child.click()
print("Going to add Child.....")

# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/name"))')
print("Scrolled down to add child DOB...")

add_child = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/name")))
add_child.send_keys("niveditha raj")
print("Going to add Child Name.....")

# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/radio_no"))')
print("Scrolled down to add child DOB...")

child_dob = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/radio_no")))
child_dob.click()
print("Going to add Child DOB.....")

child_year = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageYear")))
child_year.send_keys(2)
child_year.click()
print("Going to add Year.....")

child_month = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageMonth")))
child_month.send_keys(1)
child_month.click()
print("Going to add Month.....")

# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/beneficiarygender"))')
print("Scrolled down to add child DOB...")

child_gender_select = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/beneficiarygender")))
child_gender_select.click()
print("Going to Select Child Gender.....")

child_gender = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Male"]')))
child_gender.click()
print("Going to add Child Gender.....")

child_add = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/saveData")))
child_add.click()
print("Going to add Child.....")


# HouseHold Edit
Household_edit = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/editBeneFac")))
Household_edit.click()
print("Going to edit the Household Edit.....")
location_edit = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/edit")))
location_edit.click()
Location_level = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/locationlevel")))
Location_level.click()
location_region = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Rural"]')))
location_region.click()
location_state = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholdstate")))
location_state.click()
location_state_value = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Tamil Nadu"]')))
location_state_value.click()
housrholddistrict = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholddistrict")))
housrholddistrict.click()
housrholddistrict_value = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Ramanathapuram"]')))
housrholddistrict_value.click()
housrholdtaluk = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholdtaluk")))
housrholdtaluk.click()
housrholdtaluk_value = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Kadaladi"]')))
housrholdtaluk_value.click()
housrholdgrampanchayat = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholdgrampanchayat")))
housrholdgrampanchayat.click()
housrholdgrampanchayat_values = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Siraikulam"]')))
housrholdgrampanchayat_values.click()
housrholdvillage = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholdvillage")))
housrholdvillage.click()
housrholdvillage_values = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="S.Kamarajapuram"]')))
housrholdvillage_values.click()
housrholdhamlet = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/housrholdhamlet")))
housrholdhamlet.click()
housrholdhamlet_values = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="S.Kamarajapuram"]')))
housrholdhamlet_values.click()
no_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/radio_no")))
no_button.click()

# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/address1"))')
address = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/address1")))
address.send_keys("bengalore")
pincode = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/pincode")))
pincode.send_keys("876565")
saveDataButton = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/saveDataButton")))
saveDataButton.click()
name = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/name")))
name.send_keys("Kiran raj Puttur S")
name.click()
household_save = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/saveData")))
household_save.click()
print("Household Edit is Completed .....")

# Mother Edit
mother_edit = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="org.mahiti.stagingpragati:id/editTextview"])[1]')))
mother_edit.click()
print("Going to edit the Mother Edit.....")
mother_name = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/name")))
mother_name.send_keys("janani puttur M")
# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/radio_no"))')
mother_dob = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/radio_no")))
mother_dob.click()
mother_year = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageYear")))
mother_year.send_keys(46)
mother_year.click()
mother_month = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageMonth")))
mother_month.send_keys(1)
mother_month.click()
mother_save = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/saveData")))
mother_save.click()
print("Mother Edit is Done.....")

# Child Edit
child_edit = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="org.mahiti.stagingpragati:id/editTextview"])[2]')))
child_edit.click()
print("Going to Edit Child.....")
# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/name"))')
add_child = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/name")))
add_child.send_keys("niveditha raj Edit")
# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/radio_no"))')
child_dob = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/radio_no")))
child_dob.click()
child_year = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageYear")))
child_year.send_keys(3)
child_year.click()
child_month = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/ageMonth")))
child_month.send_keys(1)
child_month.click()
# scroll down
driver.find_element( AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("org.mahiti.stagingpragati:id/beneficiarygender"))')
child_gender_select = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/beneficiarygender")))
child_gender_select.click()
child_gender = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Male"]')))
child_gender.click()
child_add = wait.until(EC.presence_of_element_located((AppiumBy.ID, "org.mahiti.stagingpragati:id/saveData")))
child_add.click()
print("Child Edit is Done.....")

time.sleep(50)

# Additional interactions can be added here

driver.quit()
