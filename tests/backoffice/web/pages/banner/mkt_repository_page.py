import os

from selene import Browser
from selene.api import s
from selene.core.configuration import Config
from selene.support.conditions import have

from tests.backoffice.web.pages.backoffice_page import BackofficeBasePage
from tests.backoffice.web.pages.banner.banner_home_page import BannerHome
from tests.backoffice.web.pages.component.combobox import ComboBox


class MktRepositoryPage(BackofficeBasePage):
    def __init__(self, app: Browser):
        super().__init__(app)
        self.card_new_banner_repository = s('#NewBannerCard')
        self.btn_create_banner = self.get_elem_by_text('CRIAR BANNER').s("./..")
        self.input_calendar = s("//input[contains(@class, 'ant-calendar-input')]")

    def input_file_by_parent(self, parent):
        return parent.s("./descendant::input[@type='file']")

    def go_to_mkt_repository(self):
        if not self.app.driver.current_url.__contains__('banners/marketing-repository'):
            self.menu.access_menu('Banners')
            BannerHome(self.app).access_btn_by_text('Repositório de marketing')

    def combo_in_repository(self, label):
        combo = self.get_combo_by_label(label, self.card_new_banner_repository)
        return ComboBox(combo)

    def input_in_repository(self, label):
        return self.get_input_by_label(label, self.card_new_banner_repository)

    def input_img_new_banner(self):
        return self.input_file_by_parent(self.card_new_banner_repository)

    def fill_new_banner(self, **kwargs):
        if kwargs.get('slot'):
            self.combo_in_repository('Slot').select(kwargs.get('slot'))
        if kwargs.get('banner_type'):
            self.combo_in_repository('Tipo de Banner').select(kwargs.get('banner_type'))
            if kwargs.get('banner_type') == 'Com Link' and kwargs.get('link'):
                self.input_in_repository('Link').type(kwargs.get('link'))

    def has_banner_request(self):
        return len(self.get_banner_request_list()) > 0

    def get_banner_request_list(self):
        banners = self.get_elem_by_text('Solicitações de banner').ss("./../div")
        banners.with_(Config(timeout=12)).wait_until(have.size_greater_than(0))
        return banners

    def upload_img_banner_request(self, title='', file_path=None):
        in_upload = None
        if title != '':
            for banner in self.get_banner_request_list():
                banner_title = banner.s("./descendant::strong").text
                if banner_title == title:
                    in_upload = self.input_file_by_parent(banner)
        else:
            in_upload = self.input_file_by_parent(self.get_banner_request_list()[0])
        if in_upload is None:
            raise ValueError(f"Input '{title}' not found")
        in_upload.type(os.path.abspath(file_path))
