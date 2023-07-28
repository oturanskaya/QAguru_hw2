import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture()
def browser_size():
    browser.config.driver_name = 'firefox'
    driver = webdriver.Firefox()
    driver.set_window_size(1200, 600)

    yield

    browser.quit()
