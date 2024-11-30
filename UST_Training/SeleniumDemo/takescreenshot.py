from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path=r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/India")
driver.implicitly_wait(3)
driver.save_screenshot("indiapage.png")

search_username= driver.find_element(By.LINK_TEXT,"Indian Ocean")
print(search_username)
print(search_username.text)
driver.get(search_username.get_attribute('href'))
driver.implicitly_wait(3)
driver.save_screenshot("indian ocean.png")


time.sleep(3)

driver.quit()
