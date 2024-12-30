from htmlclass import HtmlClass
from selenium.webdriver.common.by import By
import yaml
import logging

class SearchLocators:
    ids = dict()
    with open("locators.yaml", "r") as f:
        locators = yaml.safe_load(f)
    if locators["XPATH"]:
        for locator in locators["XPATH"].keys():
            ids[locator] = (By.XPATH, locators["XPATH"][locator])
    if locators["CSS"]:
        for locator in locators["CSS"].keys():
            ids[locator] = (By.CSS_SELECTOR, locators["CSS"][locator])


class OperationsHelper(HtmlClass):
    def check_success_login(self):
        return self.find_element(SearchLocators.ids["LOCATOR_SUCCESS_LOGIN"]).text

    def enter_login(self, login):
        logging.info(f"Send '{login}' to element {SearchLocators.ids['LOCATOR_LOGIN_FIELD']}")
        login_field = self.find_element(SearchLocators.ids["LOCATOR_LOGIN_FIELD"])
        if not login_field:
            logging.error("Login field not found")
            return False
        try:
            login_field.clear()
            login_field.send_keys(login)
        except:
            logging.exception("Exception while operation with login field")


    def enter_password(self, password):
        password_field = self.find_element(SearchLocators.ids["LOCATOR_PASSWORD_FIELD"])
        if not password_field:
            logging.error("Password field not found")
            return False
        try:
            password_field.clear()
            password_field.send_keys(password)
        except:
            logging.exception("Exception while operation with password field")

    def click_login_button(self, wait=False):
        try:
            self.find_element(SearchLocators.ids["LOCATOR_LOGIN_BUTTON"]).click()
            if wait:
                self.wait_element_stay_invisible(SearchLocators.ids["LOCATOR_LOGIN_BUTTON"])
        except:
            logging.exception("Exception while click login button")

    def get_error_message(self):
        try:
            error_text = self.find_element(SearchLocators.ids["LOCATOR_ERROR_FIELD"]).text
            return error_text
        except:
            return None

    def click_about_link(self):
        try:
            self.find_element(SearchLocators.ids["LOCATOR_ABOUT_LINK"]).click()
        except:
            logging.exception("Exception while click about link")

    def get_about_title_font_size(self):
        try:
            return self.get_element_property(SearchLocators.ids["LOCATOR_ABOUT_FONT_SIZE"], "font-size")
        except:
            logging.exception("Exception while get title font size")
            return None

    def get_text_title_about(self):
        try:
            text = self.find_element(SearchLocators.ids["LOCATOR_ABOUT_FONT_SIZE"]).text
            return text
        except:
            logging.exception("Exception while get title text")
            return None
