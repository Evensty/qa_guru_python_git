from selene.support.shared import browser
from selene import be, have


s = 'short text fot test'
def test_should_be_google_search_input():
    browser.open('https://www.google.com/')
    browser.element('[name ="q"]').should(be.blank).type('habr').press_enter()
    browser.element('[id="search"]').should(have.text('Все публикации подряд'))


def test_example():
    assert 10 > 1
    assert 4 < 9


def test_another_1():
    assert 0 != 1
    assert 5 > 2


def test_another_11():
    assert 0 == 0


def test_len_of_test_string():
    assert len(s) > 10


