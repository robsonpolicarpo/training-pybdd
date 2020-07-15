import logging

from selene import Browser
from selene.api import s
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class GenericPage(object):
    TIMEOUT_DEFAULT = 15

    def __init__(self, app: Browser):
        self.app: Browser = app

    def focus(self, element):
        self.app.driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def get_elem_by_text(text):
        return s(f"//*[text()='{text}']")

    @staticmethod
    def get_element_by_contains_text(text):
        return s(f"//*[contains(text(), '{text}')]")

    def get_webdriver_wait(self, timeout=TIMEOUT_DEFAULT):
        return WebDriverWait(self.app.driver, timeout)

    def wait_visibility(self, element, timeout=TIMEOUT_DEFAULT):
        try:
            self.get_webdriver_wait(timeout).until(ec.visibility_of(element))
            return True
        except Exception as e:
            logging.warning('Error in >wait_visibility< ' + str(e))
            return False

    def wait_invisibility(self, element, timeout=TIMEOUT_DEFAULT):
        try:
            self.get_webdriver_wait(timeout).until(ec.invisibility_of_element(element))
        except Exception as e:
            logging.warning('Error in >wait_invisibility< ' + str(e))

    def wait_clickable(self, element, timeout=TIMEOUT_DEFAULT):
        self.get_webdriver_wait(timeout).until(ec.element_to_be_clickable(element))

    def get_shadow_element(self, root_element: WebElement) -> WebElement:
        elem = self.app.driver.execute_script("return arguments[0].shadowRoot", root_element)
        return elem
