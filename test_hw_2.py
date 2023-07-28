from selene.support.shared import browser
from selene import be, have


def test_valid_query(browser_size):
    browser.open('https://google.com')
    browser.element('[name=q]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text("yashaka/selene: User-oriented Web UI browser tests in Python"))


def test_invalid_query(browser_size):
    browser.open('https://google.com')
    browser.element('[name=q]').should(be.blank).type('jshwgwkckcjdhegh').press_enter()
    browser.element('#res').should(have.text("По запросу jshwgwkckcjdhegh ничего не найдено."))