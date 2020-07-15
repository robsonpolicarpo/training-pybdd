from selene import config as _selene_config
from selenium.webdriver import DesiredCapabilities

from . import env
from .env import get_args

ONE_SESSION = env.get_bool('ONE_SESSION', 'False')
BROWSER_LOGS = env.get_bool('BROWSER_LOGS', 'False')

_selene_config.timeout = int(env.get('UI_TIMEOUT', 15))
APPIUM_TIMEOUT = int(env.get('APPIUM_TIMEOUT', 600))


class TestRun:

    @staticmethod
    def platform():
        return str(get_args().platform).upper()

    @staticmethod
    def is_remote():
        return str(get_args().remote).lower() == 'true'

    @staticmethod
    def is_web():
        return TestRun.platform() == 'LINUX'

    @staticmethod
    def is_mobile():
        return TestRun.platform() in ('IOS', 'ANDROID')

    @staticmethod
    def is_android():
        return TestRun.platform() == 'ANDROID'

    @staticmethod
    def cap(platform=''):
        cap = {
            'WEB': {
                **DesiredCapabilities.CHROME,
                'loggingPrefs': {'browser': 'ALL'}
            },
            'ANDROID': {
                'version': '10.0',
                'platformName': 'Android',
                'platformVersion': '10.0',
                'deviceName': 'Android_Emulator',
                'noReset': False,
                'fullReset': False,
                'newCommandTimeout': APPIUM_TIMEOUT,
                "automationName": "UiAutomator2",
                "browserName": 'chrome'
            },
            'IOS': {
                'version': '1.8.0',
                'platformName': 'iOS',
                'platformVersion': '11.4',
                'deviceName': 'iPhone X',
                'noReset': False,
                'fullReset': False,
                'newCommandTimeout': APPIUM_TIMEOUT,
            }
        }
        return cap[platform]
