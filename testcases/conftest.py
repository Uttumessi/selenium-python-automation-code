import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(scope="class")
def setup(request, browser, url):
    if browser == "chrome":
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
    elif browser == "firefox":
        service = Service(GeckoDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
    elif browser == "edge":
        service = Service(EdgeChromiumDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
        parser.addoption("--browser")
        parser.addoption("--url")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
        return request.config.getoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def url(request):
        return request.config.getoption("--url")



    # service = Service(ChromeDriverManager().install())
    # options = webdriver.ChromeOptions()
    # options.add_argument("--disable-notifications")
    # driver = webdriver.Chrome(service=service, options=options)
    # driver.maximize_window()
    # driver.get("https://www.yatra.com/")
    # request.cls.driver = driver
    # yield
    # driver.close()

