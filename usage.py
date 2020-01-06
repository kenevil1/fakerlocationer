from fakerlocationer import FakerLocationer
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.mylocation.org")
f = FakerLocationer(driver)
f.setLocation(50, 50)
