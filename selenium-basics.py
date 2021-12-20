from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window() # Browser becomes fullscreen
# print(driver.title) Shows the website title
# driver.save_screenshot("github.com-homepage.png") # Screenshot of the browser

url = "https://github.com/M4dn4ss"
driver.get(url)

if "Samed Önder Koçak" in driver.title: # if page contains that text takes a screenshot
    driver.save_screenshot("github-samed.png")

time.sleep(2)

driver.back() # Goes back
# driver.forward()

time.sleep(2)

driver.close()