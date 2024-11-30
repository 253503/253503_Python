from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path=r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)
driver.maximize_window()

driver.get("https://demo.guru99.com/test/delete_customer.php")
search_username= driver.find_element(By.NAME,"cusid")
search_username.send_keys("gayathri")
search_username.send_keys(Keys.RETURN)


#handle the alert
alert = driver.switch_to.alert

print("Alert  txt:"+alert.text)
alert.accept()

search_username.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

