import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)
    browser_name = config['browser'].lower()
    name = config["username"]
    password = config["password"]
    url = config["url"]



@pytest.fixture(scope='session')
def browser():
    if browser_name == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def success_login():
    return f"Hello, {name}"

@pytest.fixture()
def login_fail():
    return "401"

@pytest.fixture()
def title():
    return "about page", "32px"