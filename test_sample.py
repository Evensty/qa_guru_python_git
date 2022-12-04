from selene.support.shared import browser
from selene import be


n = 5


def test_should_be_yandex_search_input():
    browser.open('https://ya.ru/')
    browser.element('#text').should(be.blank)


def test_example():
    assert 20 > 8


def test_vasya():
    assert 0 != 1


def test_another_10():
    assert 0 == 0


def test_last():
    assert 2**n < 40


