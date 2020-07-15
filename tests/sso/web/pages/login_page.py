import logging

from selene.api import s
from selene.support.conditions import be

from tests.config.generic_page import GenericPage


class LoginPage(GenericPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.form = s("#kc-form-login")
        self.input_username = s("#username")
        self.input_password = s("#password")
        self.btn_login = s("#kc-login")

    def login(self, user):
        if self.is_logged():
            return False
        self.input_username.type(user.get('username'))
        self.input_password.type(user.get('password'))
        self.btn_login.click()
        return True

    def is_logged(self):
        try:
            return not self.input_username.matching(be.visible)
        except Exception as e:
            logging.warning(e)
            return True
