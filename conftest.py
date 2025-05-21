import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    yield
    browser.quit()
