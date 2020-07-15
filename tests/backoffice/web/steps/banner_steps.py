from pytest_bdd import scenarios, when

from tests.backoffice.web.pages.banner.banner_home_page import BannerHome
from tests.backoffice.web.pages.banner.mkt_repository_page import MktRepositoryPage

scenarios(
    '../features/banners/035_banner.feature',
)


@when("estou na tela 'Repositório de marketing'")
def step_impl1(app):
    MktRepositoryPage(app).go_to_mkt_repository()


@when("acionar a opção 'Repositório de marketing'")
def step_impl2(app):
    BannerHome(app).access_btn_by_text('Repositório de marketing')
