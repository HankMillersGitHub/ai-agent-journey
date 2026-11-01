# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")  # 需要无头模式时打开
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()