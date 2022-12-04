from selene.support.shared import browser
from selene import be


def test_should_be_google_search_input():
    browser.open('https://www.google.com/')
    browser.element('[name ="q"]').should(be.blank)


def test_example_0():
    assert 10 > 1


def test_another_1():
    assert 0 != 1


def test_another_10():
    assert 0 == 0


