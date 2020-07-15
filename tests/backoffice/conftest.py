import pytest
from pytest_bdd import given, parsers

from tests.backoffice.web.pages.home_page import Home
from tests.backoffice.web.support.enuns.filepath_enum import FilePath
from tests.sso.web.pages.login_page import LoginPage
from tests.support.json_util import read_json

URL_BASE = 'https://b2b-admin-staging.devyandeh.com.br'


@pytest.fixture(scope='session')
def context():
    """Context object to store data to be shared among steps"""
    return {}


def pytest_bdd_before_scenario(request, feature, scenario):
    """Called before scenario is executed."""


def pytest_bdd_after_scenario(request, feature, scenario):
    """Called after scenario is executed."""
    add_scenario_to_run(request, scenario)
    pytest.globalDict['last_run'] = {feature.name: scenario.name}


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """Called when step function failed to execute."""
    scenario.exception = exception
    scenario.failed = True
    flag = False
    for scenario_step in scenario.steps:
        scenario_step.failed = None if flag else False
        if scenario_step == step:
            scenario_step.exception = exception
            scenario_step.failed = True
            flag = True
    driver = pytest.globalDict.get('_driver')
    if driver:
        step.attach(driver.get_screenshot_as_base64(), media_type='image/png')
    if request.config.option.export_results == 'true':
        add_scenario_to_run(request, scenario)
    pytest.globalDict['last_run'] = {feature.name: scenario.name}


def add_scenario_to_run(request, scenario):
    scenario.data_set = {}
    for key, value in request.node.funcargs.items():
        if key in scenario.params:
            scenario.data_set.update({key: value})
    suite_name = scenario.feature.name.split(' - ')[0]
    if suite_name not in pytest.globalDict['scenarios_run']:
        pytest.globalDict['scenarios_run'][suite_name] = []
    pytest.globalDict['scenarios_run'][suite_name].append(scenario.name)
    # deepcopy(scenario)


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
    else:
        login_page.login(users['b2b'])


@given(parsers.parse('na tela inicial acionar o card "{option}"'))
def step_impl2(app, context, option):
    Home(app).access_card(option)
