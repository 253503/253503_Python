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
element=driver.find_element(By.CLASS_NAME,"adv_hed")
element.scrollIntoView()
driver.implicitly_wait(3)
driver.save_screenshot("i1.png")


time.sleep(3)

driver.quit()
