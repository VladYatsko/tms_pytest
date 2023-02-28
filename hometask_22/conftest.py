import pytest
from selenium import webdriver


@pytest.fixture()
def setup_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.close()
