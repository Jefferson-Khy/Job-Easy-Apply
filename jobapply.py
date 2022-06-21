from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


username = "Enter your email here"
password = "Enter your password here"

# you have to change the path to your stuff
chrome_driver_path="Enter the path of the chromedriver or (whatever browser driver you have installed) here"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3123986810&distance=25.0&f_AL=true&f_E=2&f_WT=2&geoId=103644278&keywords=software%20developer&location=United%20States&refresh=true")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()
email_field = driver.find_element_by_id("username")
email_field.send_keys(username)

password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)


all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(1.5)
    apply_button = driver.find_element_by_css_selector(".jobs-s-apply")
    if not apply_button:
        continue
    else:
        apply_button.click()
        time.sleep(1.5)
    button = driver.find_element_by_css_selector(".artdeco-button--primary")
    while button:
        button = driver.find_element_by_css_selector(".artdeco-button--primary")
        button.click()
        time.sleep(2)
    
  
