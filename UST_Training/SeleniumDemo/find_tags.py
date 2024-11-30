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
#search_username= driver.find_elements(By.TAG_NAME,"a")
# for link in search_username:
#     print(link.text)



search_username= driver.find_element(By.LINK_TEXT,"Indian Ocean")
print(search_username)
print(search_username.text)




driver.get(search_username.get_attribute('href'))

#forward and backward links
driver.implicitly_wait(5)
driver.back()
driver.implicitly_wait(5)
driver.forward()


time.sleep(3)

driver.quit()
