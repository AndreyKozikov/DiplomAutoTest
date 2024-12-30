import time

from utilities import OperationsHelper
import yaml

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)
    username = config['username']
    password = config['password']
    url = config['url']

def test_invalid_login(browser, login_fail):
    test_page = OperationsHelper(browser)
    test_page.get_web_page(url + "login")
    test_page.enter_login(login_fail[0])
    test_page.enter_password(login_fail[1])
    test_page.click_login_button(False)
    err = test_page.get_error_message()
    browser.save_screenshot("screenshots/invalid_login.png")
    assert err == login_fail

def test_login(browser, success_login):
    test_page = OperationsHelper(browser)
    test_page.get_web_page(url)
    test_page.enter_login(username)
    test_page.enter_password(password)
    browser.save_screenshot("screenshots/success_login.png")
    test_page.click_login_button(True)
    greeting = test_page.check_success_login()
    assert greeting == success_login

def test_about_title_properties(browser, title):
    test_page = OperationsHelper(browser)
    test_page.click_about_link()
    time.sleep(3)
    text = test_page.get_text_title_about()
    if text.lower() == title[0]:
        font_size_title = test_page.get_about_title_font_size()
        browser.save_screenshot("screenshots/about_page.png")
        assert font_size_title == title[1]
    else:
        assert False




