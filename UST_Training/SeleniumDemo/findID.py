from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path=r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)

# driver.get("https://www.practicetestautomation.com/practice-test-login")

#BY ID************
# search_username= driver.find_element(By.ID,"username")
# search_username.send_keys("student")
# search_pass= driver.find_element(By.ID,"password")
# search_pass.send_keys("Password123")
# search_submit= driver.find_element(By.ID,"submit")
# search_submit.click()


# BY NAME ***********
# driver.get("https://www.github.com/login")
# search_username= driver.find_element(By.NAME,"login")
# search_username.send_keys("student")
# search_pass= driver.find_element(By.NAME,"password")
# search_pass.send_keys("Password123")
# driver.implicitly_wait(5)
# search_pass.send_keys(Keys.RETURN)



# BY CLASS ***********
driver.get("https://www.github.com/login")
search_username= driver.find_element(By.CLASS_NAME,"form-control input-block js-login-field")
search_username.send_keys("student")
search_pass= driver.find_element(By.CLASS_NAME,"form-control form-control input-block js-password-field")
search_pass.send_keys("Password123")
driver.implicitly_wait(5)
search_pass.send_keys(Keys.RETURN)

print("Title is:"+driver.title)


time.sleep(7)

driver.quit()
