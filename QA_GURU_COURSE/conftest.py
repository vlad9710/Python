import pytest
from selene.support.shared import browser
from selene import by, be, have


@pytest.fixture()
def browser_open():
    browser.open("https://google.com").driver.maximize_window()