import logging
import os

import pytest


def get(key, default=None):
    return os.environ.get(key=key, default=default)


def get_args():
    try:
        return pytest.globalDict.get('args')
    except Exception as e:
        logging.warning(e)
        return None


def get_bool(key, default=None):
    value = get(key, default)
    return f'{value}'.lower() == 'true'
