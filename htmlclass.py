import yaml
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)


class HtmlClass:
    def __init__(self, driver, ):
        self.driver = driver

    def find_element(self, locator, time=20):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                     message=f'Element {locator} not found')
        except Exception:
            logging.exception(f'Element {locator} find exception.')
            return None

    def wait_element_stay_invisible(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def get_element_property(self, locator, prop):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(prop)
        else:
            logging.error(f'Property {prop} not found in element {locator}')
            return None

    def get_element_value(self, locator):
        element = self.find_element(locator)
        if element:
            return element.get_attribute('value')
        else:
            logging.error(f'Element {locator} not found.')
            return None

    def get_web_page(self, url):
        try:
            return self.driver.get(url)
        except:
            logging.exception(f'Exception while trying to open {url}.')
            return None