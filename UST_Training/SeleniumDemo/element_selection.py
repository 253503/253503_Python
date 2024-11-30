from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path=r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)

driver.get("https://www.duckduckgo.com")

search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

print("Title is:"+driver.title)


time.sleep(7)

driver.quit()
