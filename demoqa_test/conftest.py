import pytest
from selene import browser

@pytest.fixture
def browser_config():
    browser.config.window_height = 980
    browser.config.window_width = 670
    return browser