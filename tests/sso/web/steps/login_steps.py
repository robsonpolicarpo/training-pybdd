from pytest_bdd import scenarios, given

from tests.backoffice.conftest import URL_BASE
from tests.backoffice.web.support.enuns.filepath_enum import FilePath
from tests.sso.web.pages.login_page import LoginPage
from tests.support.json_util import read_json

scenarios(
    '../features/008_login.feature',
)


@given('que esteja logado no B2B Admin')
def step_impl1(app):
    users = read_json(FilePath.USERS_ADMIN.value)
    login_page = LoginPage(app)
    if app.config.base_url == '':
        app.config.base_url = URL_BASE
    if app.driver.current_url != app.config.base_url + '/':
        app.open(app.config.base_url)
    if login_page.is_logged():
        return
    assert login_page.login(users['b2b'])
