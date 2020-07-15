from selene.api import ss
from selene.core.configuration import Config
from selene.support.conditions import be, have


class MsgTopRight:

    def __init__(self):
        self.list_msg = ss("//div[contains(@class, 'ant-notification-topRight')]/span")

    def last_msg(self):
        return self.list_msg[-1].s("./*")

    def is_visible(self, timeout=3):
        return self.last_msg().with_(Config(timeout=timeout)).wait_until(be.visible)

    def get_msg_top_right(self, timeout=3):
        if self.is_visible(timeout):
            return self.last_msg().get_attribute('innerText')

    def verify_msg(self, msg_txt, timeout=7, throw_exc=False):
        if self.is_visible(timeout):
            assert self.last_msg().with_(
                Config(timeout=timeout)).wait_until(
                have.attribute('innerText').value_containing(msg_txt))
        elif throw_exc:
            raise ValueError("Toast not presented")

    def close_last(self):
        btn_close = self.last_msg().s(
            "./descendant::a[contains(@class, 'ant-notification-notice-close')]")
        btn_close.click()

    def close_by_text(self, text, timeout=3):
        self.list_msg.with_(Config(timeout=timeout)).wait_until(have.size_greater_than(0))
        for msg in self.list_msg:
            if msg.s("./*").get_attribute('innerText').__contains__(text):
                btn_close = msg.s(
                    "./descendant::a[contains(@class, 'ant-notification-notice-close')]")
                btn_close.click()
