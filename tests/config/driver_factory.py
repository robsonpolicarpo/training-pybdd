"""Driver Factory"""
import os
from os import path

import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from tests.config.env import get_args
from tests.config.test_run import TestRun


def get_browser():
    driver = get_selenium_driver()
    browser.config.driver = driver
    browser.config.browser_name = 'chrome'
    browser.config.timeout = 7
    browser.config.save_page_source_on_failure = False
    browser.config.save_screenshot_on_failure = False
    pytest.globalDict['_driver'] = driver
    return browser


def close(driver):
    driver.close_app() if TestRun.is_mobile() else driver.quit()


def get_selenium_driver():
    if TestRun.is_remote():
        if TestRun.is_mobile():
            return get_mobile_driver(iprun=get_args().ipenv)
        return get_remote_chrome(get_args().ipenv)
    else:
        if TestRun.is_mobile():
            return get_mobile_driver(app_name=get_args().application)
        return get_local_chrome()


def get_local_chrome(path_driver=''):
    if path_driver and path.exists(path_driver):
        return webdriver.Chrome(path_driver, chrome_options=get_options_chrome())
    else:
        return webdriver.Chrome(chrome_options=get_options_chrome())


def get_remote_chrome(ipenv):
    return webdriver.Remote(
        command_executor=f"http://{ipenv}:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME,
        options=get_options_chrome())


def get_mobile_driver(iprun=None, app_name='chrome'):
    if iprun:
        command_executor = f"http://{iprun}:4444/wd/hub"
    else:
        command_executor = "http://localhost:4723/wd/hub"
    cap = TestRun.cap(TestRun.platform())
    if app_name == 'chrome':
        cap['chromeOptions'] = get_options_chrome_mobile()
    else:
        cap['app'] = os.path.abspath("./mobile_app/" + app_name)

    return webdriver.Remote(command_executor=command_executor, desired_capabilities=cap)


def get_options_chrome_mobile():
    return {'args': ['--no-sandbox']}


def get_options_chrome():
    options = Options()
    options.add_argument("test-type")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-infobars')
    options.add_argument('--no-sandbox')
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("window-size=1920, 1080")
    options.headless = get_args().headless in ("True", "true", True)
    return options
