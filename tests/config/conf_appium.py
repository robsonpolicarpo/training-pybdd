import os
import copy
import datetime

import pytest

from tests.support.file_util import ensure_dir


class AppiumConf:
    def __init__(self):
        today = '{:%Y_%m_%d_%H_%S}'.format(datetime.datetime.now())
        result_dir = os.path.join(os.path.dirname(__file__), 'results', today)
        ensure_dir(result_dir)
        result_dir_test_run = result_dir
        ensure_dir(os.path.join(result_dir_test_run, 'screenshots'))
        ensure_dir(os.path.join(result_dir_test_run, 'logcat'))

    def androidcapabilities(self, app_name):
        caps = {}  #  copy.copy(settings.ANDROID_BASE_CAPS)
        caps['app'] = os.path.realpath('b2b_experience_test/mobile_app/' + app_name)
        return caps

    def webcapabilities(self, browser_name):
        caps = {}  # copy.copy(settings.ANDROID_BASE_CAPS)
        caps['chromeOptions'] = {'args': ['--no-sandbox']}
        caps['browserName'] = browser_name
        return caps

    def ioscapabilities(self, app_name):
        """implement"""


class DeviceLogger:
    def __init__(self, logcat_dir, screenshot_dir):
        self.screenshot_dir = screenshot_dir
        self.logcat_dir = logcat_dir


@pytest.fixture(scope='function')
def device_logger(request):
    logcat_dir = request.config.logcat_dir
    screenshot_dir = request.config.screen_shot_dir
    return DeviceLogger(logcat_dir, screenshot_dir)
