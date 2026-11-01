from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service())
driver.get("https://www.baidu.com")
print(driver.current_url)
driver.quit()