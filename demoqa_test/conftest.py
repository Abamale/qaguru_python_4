# from distutils.command.config import config

#from selene.support import config

import pytest
from selene import browser


@pytest.fixture
def browser_config():
    browser.config.window_height = 700
    browser.config.window_width = 660
    browser.config.base_url = 'https://demoqa.com'
    return browser
