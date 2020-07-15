import os

from selene import Browser
from selene.api import s
from selene.core.configuration import Config
from selene.support.conditions import be

from tests.backoffice.web.pages.backoffice_page import BackofficeBasePage
from tests.backoffice.web.pages.component.combobox import ComboBox
from tests.backoffice.web.support.enuns.filepath_enum import FilePath


class BannerHome(BackofficeBasePage):

    def __init__(self, app: Browser):
        super().__init__(app)
        self.btn_supplier_banner = s('#supplier-banner-modal')
        self.card_new_banner_repository = s('#NewBannerCard')

    def access_btn_by_text(self, btn_title):
        if btn_title == 'Novo banner de fornecedor':
            self.btn_supplier_banner.click()
            self.modal.wait_modal_title_presented(btn_title)
        else:
            btn = self.get_elem_by_text(btn_title).s('./..')
            assert btn.with_(Config(timeout=12)).wait_until(be.clickable)
            btn.click()
            if btn_title == 'Novo banner de simulador de margem':
                self.modal.wait_modal_title_presented(btn_title)

    def combo_supplier(self):
        combo = self.modal.combo_by_title('Fornecedor')
        return ComboBox(combo)

    def combo_validity(self):
        combo = self.modal.combo_by_title('Período de vigência')
        return ComboBox(combo)

    def combo_action_audience(self):
        combo = self.modal.combo_by_title('Público da ação')
        return ComboBox(combo)

    def input_initial_date(self):
        return self.modal.content.s(
            "./descendant::*[text()='Data de início']/../following-sibling::*/descendant::input")

    def input_end_date(self):
        return self.modal.content.s(
            "./descendant::*[text()='Data de término']/../following-sibling::*/descendant::input")

    def fill_new_banner_popup(self, **kwargs):
        if kwargs.get('supplier'):
            self.combo_supplier().select(kwargs.get('supplier'))
        if kwargs.get('validity'):
            self.combo_validity().select(kwargs.get('validity'))
        if kwargs.get('initial_date'):
            self.input_initial_date().with_(Config(
                set_value_by_js=True)).set_value(kwargs.get('initial_date'))
        if kwargs.get('validity') == 'Personalizado':
            self.input_end_date().with_(Config(
                set_value_by_js=True)).set_value(kwargs.get('end_date'))
        if kwargs.get('action_audience'):
            self.combo_action_audience().select(kwargs.get('action_audience'))
            if kwargs.get('action_audience') == 'Subir lista':
                self.upload_stores()

    def upload_stores(self):
        self.modal.btn_by_title('SUBIR LISTA DE LOJAS').click()
        upload_area_selector = self.modal.content.s("./descendant::input[@type='file']")
        upload_area_selector.type(os.path.abspath(FilePath.STORES.value))
        upload_stores_list_tags = self.modal.content.s("//*[contains(@class, 'UploadTags_fileIte')]")
        assert upload_stores_list_tags.wait_until(be.clickable)
        self.modal.confirm()

    def combo_repository(self, label):
        combo = self.get_combo_by_label(label, self.card_new_banner_repository)
        return ComboBox(combo)

    def input_repository(self, label):
        return self.get_input_by_label(label, self.card_new_banner_repository)
