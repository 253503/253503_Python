from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path=r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)
driver.maximize_window()

driver.get("https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI")
element=driver.find_element(By.CLASS_NAME,"adv_arv")
driver.execute_script("arguments[0].scrollIntoView();",element)
driver.execute_script("arguments[0].scrollIntoView();",element)
driver.execute_script("arguments[0].scrollIntoView();",element)
driver.implicitly_wait(10)
#time.sleep(20)
driver.save_screenshot("ShareMarketChart.jpg")
driver.implicitly_wait(10)
#time.sleep(10)
print('Done')

#driver.implicitly_wait(10)
time.sleep(10)

driver.quit()