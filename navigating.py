from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

url = "https://www.youtube.com/"
driver.get(url)

searchInput = driver.find_element_by_name("search_query")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
# result = driver.page_source


# result = driver.find_element_by_css_selector(".title h3 a")

# for element in result:
#     print(element.text)

driver.close()