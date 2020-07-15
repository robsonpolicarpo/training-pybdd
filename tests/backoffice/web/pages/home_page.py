from selene import Browser
from selene.api import s

from tests.backoffice.web.pages.backoffice_page import BackofficeBasePage


class Home(BackofficeBasePage):
    def __init__(self, app: Browser):
        super().__init__(app)
        self.card_campaign = s('#CampaignsPage')
        self.card_banners = s('#BannersPage')

    def go_to_campaigns_page(self):
        s("//a[@href='/campaigns']").click()

    def access_card(self, card_title):
        if card_title == 'Ações de vendas':
            self.card_campaign.click()
        elif card_title == 'Banners':
            self.card_banners.click()
