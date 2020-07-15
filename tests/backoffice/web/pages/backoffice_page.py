from selene import Browser
from selene.api import s
from selene.core.entity import Element

from tests.backoffice.web.test_data.data_backoffice import DataB2BAdmin
from tests.backoffice.web.pages.component.menu import Menu
from tests.backoffice.web.pages.component.modal import Modal
from tests.backoffice.web.pages.component.msg_top_right import MsgTopRight
from tests.config.generic_page import GenericPage


class BackofficeBasePage(GenericPage):

    def __init__(self, app: Browser):
        super().__init__(app)
        self.fakedata = DataB2BAdmin()
        self.menu = Menu()
        self.modal = Modal(app)
        self.msg_top_right = MsgTopRight()

    def get_combo_by_label(self, label: str, parent_base: Element = None):
        if parent_base:
            return parent_base.s(f"./descendant::*[text()='{label}']/following-sibling::div/div")
        else:
            return s(f"//*[text()='{label}']/following-sibling::div/div")

    def get_input_by_label(self, label: str, parent_base: Element = None):
        if parent_base:
            label_elem = parent_base.s(f"./descendant::*[text()='{label}']")
        else:
            label_elem = self.get_elem_by_text(label)
        return label_elem.s("./ancestor::div[1]/descendant::input")
