from selene.api import s


class Menu:
    def __init__(self):
        self.btn_sandwich = s("//button[contains(@class, 'ContentHeader_menuButton*')]")
        self.options = s("//*[@id='root']/section/div").ss("./descendant::ul/li")

    def access_menu(self, item):
        self.btn_sandwich.click()
        for option in self.options:
            op_text = option.s("./descendant::span").text
            if op_text == item:
                option.s("./descendant::a").click()
                return
        raise ValueError(f"Value '{item}' not found in menu")
