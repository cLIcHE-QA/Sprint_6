import pytest
from selenium import webdriver

from data import Urls

urls = Urls()


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.get(urls.MAIN_URL)

    yield driver
    driver.quit()
