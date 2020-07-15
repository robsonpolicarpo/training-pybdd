import time

from selene.api import ss
from selene.core.configuration import Config
from selene.core.entity import Element
from selene.support.conditions import be, have


class ComboBox:

    def __init__(self, combo: Element):
        self.combo = combo

    def options(self):
        return ss("//*[contains(@class, 'ant-select-dropdown') "
                  "and not(contains(@class, 'ant-select-dropdown-hidden'))]/div/ul/li")

    def select(self, value, partial_text: bool = False):
        assert self.combo.with_(Config(timeout=20)).wait_until(be.clickable)
        if value and value != self.get_value_selected():
            self.combo.click()
            time.sleep(0.3)
            assert self.options().with_(
                Config(timeout=15)).wait_until(have.size_greater_than(0))
            if isinstance(value, int):
                self.select_option_by_index(value)
            elif isinstance(value, str):
                if partial_text:
                    self.select_option_by_partial_text(value)
                else:
                    self.select_option_by_text(value)
            else:
                raise ValueError(f"Type not implemented for combobox item: {value}")

    def select_option_by_index(self, value: int):
        self.options()[value].click()

    def select_option_by_text(self, value: str):
        for option in self.options():
            if option.text == value:
                option.click()
                return
        options_text = self.options()[0].s('./..').get_attribute('innerText')
        raise ValueError(f"Value '{value}' not found in options:" + f"\n{options_text}")

    def select_option_by_partial_text(self, value: str):
        for option in self.options():
            if option.text.__contains__(value):
                option.click()
                return
        raise ValueError("Valeu not found in options: " + value)

    def get_value_selected(self):
        return self.combo.text

