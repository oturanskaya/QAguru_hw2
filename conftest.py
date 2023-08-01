import pytest
from selene import browser


@pytest.fixture()
def browser_size():
    browser.config.driver_name = 'firefox'
    browser.config.window_height = 1200
    browser.config.window_width =1400

    yield

    browser.quit()