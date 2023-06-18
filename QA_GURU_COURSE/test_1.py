from selene.support.shared import browser
from selene import by, be, have
import conftest


def test_positive_1(browser_open):
    browser.element(by.name("q")).should(be.blank).type("selene").press_enter()
    browser.element(by.id("search")).should(have.text("yashaka/selene: User-oriented Web UI browser tests in"))


def test_negative_1(browser_open):
    browser.element('[class="gLFyf"]').should(be.blank).type("asdghagsydgkaysgdyla").press_enter()
    browser.element('[class="s6JM6d"]').should(have.text("По запросу asdghagsydgkaysgdyla ничего не найдено. "))
