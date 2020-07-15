from selene import Config, Browser
from selene.api import s, ss
from selene.support.conditions import be

from tests.config.generic_page import GenericPage


class Modal(GenericPage):
    def __init__(self, app: Browser):
        super().__init__(app)
        self.wrapper = ss("//div[contains(@class, 'ant-modal-wrap')  and not(@style='display: none;')]")[-1]
        self.content = self.wrapper.s("./descendant::div[@class='ant-modal-content']")
        self.modal_footer = self.wrapper.s("./descendant::div[@class='ant-modal-footer']")

    def wait_modal_title_presented(self, title=''):
        title_elem = self.content.s("./descendant::*[@class='ant-modal-title']/*")
        assert title_elem.with_(Config(timeout=15)).wait_until(be.visible)
        if title != '':
            assert title_elem.text == title

    def confirm(self, button_txt: str = 'OK'):
        btn_confirm_modal = self.content.s(
            f"./descendant::button/span[text()='{button_txt}']/..")
        assert btn_confirm_modal.with_(Config(timeout=59)).wait_until(be.clickable)
        self.focus(btn_confirm_modal())
        btn_confirm_modal.click()

    def wait_modal_hidden(self, timeout=4):
        return self.wrapper.with_(Config(timeout=timeout)).wait_until(be.hidden)

    def btn_by_title(self, btn_title):
        return self.content.s(f"./descendant::*[contains(text(),'{btn_title}')]/..")

    def cancel(self):
        self.btn_by_title('CANCELAR').click()

    def close(self):
        self.content.s("./descendant::button[@class='ant-modal-close']").click()

    def wait_text_body(self, text, timeout=20, throw_exception=True):
        msg = self.content.s(f"./descendant::*[contains(text(), '{text}')]")
        result = msg.with_(Config(timeout=timeout)).wait_until(be.visible)
        if not result and throw_exception:
            raise ValueError("Mensagem não encontrada: " + text)
        return result

    def close_modal_clicking_outside_of_modal(self):
        modal_wrapper = s("//*[contains(@class, 'ant-modal-wrap')]")
        modal_wrapper.wait_until(be.clickable)
        modal_wrapper.click()

    def combo_by_title(self, title):
        return self.content.s(
            f"//*[text()='{title}']/following-sibling::div/div")
